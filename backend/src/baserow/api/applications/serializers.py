from django.utils.functional import lazy

from drf_spectacular.openapi import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from baserow.api.workspaces.serializers import WorkspaceSerializer
from baserow.core.db import specific_iterator
from baserow.core.models import Application
from baserow.core.registries import application_type_registry


class ApplicationSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    # GroupDeprecation
    group = WorkspaceSerializer(
        source="workspace",
        help_text="DEPRECATED: Please use the functionally identical "
        "`workspace` instead as this field is "
        "being removed in the future.",
    )
    workspace = WorkspaceSerializer(
        help_text="The workspace that the application belongs to."
    )

    class Meta:
        model = Application
        fields = (
            "id",
            "name",
            "order",
            "type",
            "group",  # GroupDeprecation
            "workspace",
        )
        extra_kwargs = {"id": {"read_only": True}}

    @extend_schema_field(OpenApiTypes.STR)
    def get_type(self, instance):
        return application_type_registry.get_by_model(instance.specific_class).type


class SpecificApplicationSerializer(ApplicationSerializer):
    def to_representation(self, instance):
        specific_instance = instance.specific
        return get_application_serializer(
            specific_instance, context=self.context
        ).to_representation(specific_instance)


class ApplicationCreateSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(
        choices=lazy(application_type_registry.get_types, list)()
    )
    init_with_data = serializers.BooleanField(default=False)

    class Meta:
        model = Application
        fields = ("name", "type", "init_with_data")


class ApplicationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ("name",)


class OrderApplicationsSerializer(serializers.Serializer):
    application_ids = serializers.ListField(
        child=serializers.IntegerField(),
        help_text="Application ids in the desired order.",
    )


def get_application_serializer(instance, **kwargs):
    """
    Returns an instantiated serializer based on the instance class type. Custom
    serializers can be defined per application type. This function will return the one
    that is set else it will return the default one.

    :param instance: The instance where a serializer is needed for.
    :type instance: Application
    :return: An instantiated serializer for the instance.
    :rtype: ApplicationSerializer
    """

    application = application_type_registry.get_by_model(instance.specific_class)
    serializer_class = application.instance_serializer_class

    if not serializer_class:
        serializer_class = ApplicationSerializer

    context = kwargs.pop("context", {})

    context["application"] = application

    return serializer_class(instance, context=context, **kwargs)


class InstallTemplateJobApplicationsSerializer(serializers.JSONField):
    def to_representation(self, value):
        application_ids = super().to_representation(value)

        if not application_ids:
            return None

        applications = specific_iterator(
            Application.objects.select_related("content_type", "workspace").filter(
                pk__in=application_ids, workspace__trashed=False
            )
        )
        return [get_application_serializer(app).data for app in applications]

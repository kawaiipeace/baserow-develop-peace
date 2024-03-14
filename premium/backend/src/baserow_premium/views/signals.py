from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from baserow_premium.license.features import PREMIUM
from baserow_premium.license.handler import LicenseHandler
from baserow_premium.views.models import OWNERSHIP_TYPE_PERSONAL

from baserow.contrib.database.fields import signals as field_signals
from baserow.contrib.database.fields.models import FileField, SingleSelectField
from baserow.contrib.database.views import signals as view_signals
from baserow.contrib.database.views.models import OWNERSHIP_TYPE_COLLABORATIVE
from baserow.core.exceptions import PermissionDenied
from baserow.core.models import Workspace

from .handler import delete_personal_views
from .models import KanbanView

User = get_user_model()


@receiver(field_signals.field_deleted)
def field_deleted(sender, field, **kwargs):
    if isinstance(field, FileField):
        KanbanView.objects.filter(card_cover_image_field_id=field.id).update(
            card_cover_image_field_id=None
        )
    if isinstance(field, SingleSelectField):
        KanbanView.objects.filter(single_select_field_id=field.id).update(
            single_select_field_id=None
        )


def premium_check_ownership_type(
    user: AbstractUser, workspace: Workspace, ownership_type: str
) -> None:
    """
    Checks whether the provided ownership type is supported for the user.

    Should be replaced with a support for creating views
    in the ViewOwnershipPermissionManagerType once it is possible.

    :param user: The user on whose behalf the operation is performed.
    :param workspace: The workspace for which the check is performed.
    :param ownership_type: View's ownership type.
    :raises PermissionDenied: When not allowed.
    """

    premium = LicenseHandler.user_has_feature(PREMIUM, user, workspace)

    if premium:
        if ownership_type not in [
            OWNERSHIP_TYPE_COLLABORATIVE,
            OWNERSHIP_TYPE_PERSONAL,
        ]:
            raise PermissionDenied()
    else:
        if ownership_type != OWNERSHIP_TYPE_COLLABORATIVE:
            raise PermissionDenied()


@receiver(view_signals.view_created)
def view_created(sender, view, user, **kwargs):
    workspace = view.table.database.workspace
    premium_check_ownership_type(user, workspace, view.ownership_type)


def before_user_permanently_deleted(sender, instance, **kwargs):
    delete_personal_views(instance.id)


def connect_to_user_pre_delete_signal():
    pre_delete.connect(before_user_permanently_deleted, User)


__all__ = [
    "field_deleted",
    "view_created",
    "connect_to_user_pre_delete_signal",
]

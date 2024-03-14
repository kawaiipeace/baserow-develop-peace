from django.db import models

from baserow.core.fields import AutoOneToOneField


class ThemeConfigBlock(models.Model):
    builder = AutoOneToOneField(
        "builder.Builder",
        on_delete=models.CASCADE,
        related_name="%(class)s",
    )

    class Meta:
        abstract = True


class MainThemeConfigBlock(ThemeConfigBlock):
    # colors
    primary_color = models.CharField(max_length=9, default="#5190efff")
    secondary_color = models.CharField(max_length=9, default="#0eaa42ff")
    border_color = models.CharField(max_length=9, default="#d7d8d9ff")
    # headings
    heading_1_font_size = models.SmallIntegerField(default=24)
    heading_1_color = models.CharField(max_length=9, default="#070810ff")
    heading_2_font_size = models.SmallIntegerField(default=20)
    heading_2_color = models.CharField(max_length=9, default="#070810ff")
    heading_3_font_size = models.SmallIntegerField(default=16)
    heading_3_color = models.CharField(max_length=9, default="#070810ff")

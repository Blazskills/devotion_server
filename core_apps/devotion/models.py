# Create your models here.
from core_apps.base.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class DevotionMonthDay(BaseModel):
    month = models.TextField(db_index=True,)
    day = models.TextField(db_index=True,
                           error_messages={
                               'unique_together': _("This combination of devotion month and day already exists."),
                           },
                           )

    def __str__(self):
        return f"{self.month} - {self.day}"

    class Meta:
        # Add the unique_together constraint
        unique_together = ('month', 'day')
        ordering = ['-month', 'day']


class DevotionBibleReading(BaseModel):
    devotion_month_day_id = models.ForeignKey(
        DevotionMonthDay,
        on_delete=models.CASCADE,
        related_name="devotion_month_day_id",
    )
    bible_reading_arrangement = models.PositiveIntegerField(
        verbose_name=_("Bible Reading Arrangement"),
        error_messages={
            'unique_together': _("This combination of devotion month day and Bible Reading Arrangement already exists."),
        },
    )
    bible_reading_number = models.PositiveIntegerField(blank=True, null=True, verbose_name=_("Bible Reading Number"))
    bible_reading = models.TextField(verbose_name=_("Bible Reading"))
    chapter = models.TextField(verbose_name=_("chapter"))
    from_verse = models.TextField(blank=True, verbose_name=_("From Verse"))
    to_verse = models.TextField(blank=True, verbose_name=_("To Verse"))

    def __str__(self):
        return f"{self.bible_reading} - {self.chapter}"

    class Meta:
        # Add the unique_together constraint
        unique_together = ('devotion_month_day_id', 'bible_reading_arrangement')

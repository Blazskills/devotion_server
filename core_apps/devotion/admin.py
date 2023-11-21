from django.contrib import admin

from core_apps.devotion.models import DevotionMonthDay, DevotionBibleReading


@admin.register(DevotionMonthDay)
class DevotionMonthDayAdmin(admin.ModelAdmin):
    list_display_links = [
        "id",
        "month",
        "day",
    ]

    list_display = (
        "id",
        "month",
        "day",
        "created",
        "updated",
        "created_by",
    )


@admin.register(DevotionBibleReading)
class DevotionBibleReadingDayAdmin(admin.ModelAdmin):
    list_display_links = [
        "id",
        "bible_reading_arrangement",
        "bible_reading_number",
        "bible_reading",
    ]

    # list_filter = ["month", ]
    list_display = (
        "id",
        "devotion_month_day_id",
        "bible_reading_arrangement",
        "bible_reading_number",
        "bible_reading",
        "chapter",
        "from_verse",
        "to_verse",
        "created",
        "updated",
        "created_by",
    )

from rest_framework import serializers
from core_apps.devotion.models import DevotionMonthDay, DevotionBibleReading
from utils.utility import UUIDRelatedField
from rest_framework.validators import UniqueTogetherValidator


class DailyDevotionMonthListSerializer(serializers.ModelSerializer):

    class Meta:
        model = DevotionMonthDay
        fields = [
            "id",
            "month",
            "day",
        ]
        


class DevotionMonthField(serializers.RelatedField):
    def to_representation(self, value):
        return value.month


class DevotionDayField(serializers.RelatedField):
    def to_representation(self, value):
        return value.day


class DailyDevotionBibleVersesListSerializer(serializers.ModelSerializer):
    devotion_month = DevotionMonthField(source='devotion_month_day_id', read_only=True)
    devotion_day = DevotionDayField(source='devotion_month_day_id', read_only=True)

    class Meta:
        model = DevotionBibleReading
        fields = [
            "id",
            "devotion_month",
            "devotion_day",
            "bible_reading_arrangement",
            "bible_reading_number",
            "bible_reading",
            "chapter",
            "from_verse",
            "to_verse",
        ]


class MonthAndBileVerseCreateSerializer(serializers.Serializer):
    MONTH_CHOICES = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]
    DAY_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
    ]

    month = serializers.ChoiceField(
        choices=MONTH_CHOICES,
        required=True,
        error_messages={
            "required": "Kindly select the month for the bible reading. It is required.",
            "invalid_choice": "Please select a valid month.",
        },
    )

    day = serializers.ChoiceField(
        choices=DAY_CHOICES,
        required=True,
        error_messages={
            "required": "Kindly select the day for the bible reading. It is required.",
            "invalid_choice": "Please select a valid day.",
        },
    )
    bible_reading_arrangement = serializers.IntegerField(
        required=True,
        allow_null=False,
        error_messages={
            "blank": "Kindly Enter the bible verse arrangement. It can not be blank",
            "null": "Kindly Enter the bible verse arrangement. It can not be null",
        },
    )
    bible_reading_number = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
        allow_null=True,
    )
    bible_reading = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        allow_null=False,
        error_messages={
            "blank": "Kindly Enter the bible name. It can not be blank",
            "null": "Kindly Enter the bible name. It can not be null",
        },
    )
    chapter = serializers.CharField(
        max_length=100,
        required=True,
        allow_blank=False,
        allow_null=False,
        error_messages={
            "blank": "Kindly Enter the bible chapter. It can not be blank",
            "null": "Kindly Enter the bible chapter. It can not be null",
        },
    )
    from_verse = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
        allow_null=True,
    )
    to_verse = serializers.CharField(
        max_length=100,
        required=False,
        allow_blank=True,
        allow_null=True,
    )

# class ListMonthAndBileVerseCreateSerializer(serializers.ListSerializer):
#     child = MonthAndBileVerseCreateSerializer()

from django.db import IntegrityError
from rest_framework.decorators import APIView
from rest_framework.response import Response

# Create your views here.
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView
from rest_framework import permissions, status
from core_apps.devotion.models import DevotionMonthDay, DevotionBibleReading
from .serializers import (DailyDevotionMonthListSerializer, DailyDevotionBibleVersesListSerializer,
                          MonthAndBileVerseCreateSerializer
                          )
from django.db.models.functions import Cast
from django.db.models import IntegerField


class TestApi(APIView):
    def get(self, request):
        data = {"status": "Account okay", "code": 200}
        return Response(data)


class MonthListView(ListAPIView):
    serializer_class = DailyDevotionMonthListSerializer
    permission_classes = []

    def get_queryset(self):
        month = self.kwargs.get('month', None)
        new_month = month.lower()
        first_letter_uppercase = new_month[0].upper()

        # Construct the uppercase month
        uppercase_month = first_letter_uppercase + new_month[1:]
        data = (
            DevotionMonthDay.objects
            .filter(month=uppercase_month)
            .annotate(day_as_integer=Cast('day', IntegerField()))
            .order_by("day_as_integer")
            .all()
        )
        # data = DevotionMonthDay.objects.filter(month=uppercase_month).all().order_by("day")
        return data

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class BibleVersesListView(ListAPIView):
    serializer_class = DailyDevotionBibleVersesListSerializer
    permission_classes = []

    def get_queryset(self):
        month = self.kwargs.get('month', '').lower().capitalize()
        day = self.kwargs.get('day', None)
        devotion_date = DevotionMonthDay.objects.filter(month=month, day=day).first()
        if devotion_date:
            # Use the related name to access DevotionBibleReading instances
            return devotion_date.devotion_month_day_id.all()

        return []

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class BibleVersesMonthCreate(APIView):
    permission_classes = []

    def post(self, request, format=None):
        # print(request.data)
        serializer = MonthAndBileVerseCreateSerializer(data=request.data, many=True)
        try:
            if serializer.is_valid():
                data_list = serializer.validated_data
                for data in data_list:
                    print(data)
                    instance, created = DevotionMonthDay.objects.get_or_create(
                        month=data.get("month"),
                        day=data.get("day"),
                    )
                    try:
                        DevotionBibleReading.objects.create(
                            devotion_month_day_id=instance,
                            bible_reading_arrangement=data.get("bible_reading_arrangement"),
                            bible_reading_number=data.get("bible_reading_number"),
                            bible_reading=data.get("bible_reading"),
                            chapter=data.get("chapter"),
                            from_verse=data.get("from_verse"),
                            to_verse=data.get("to_verse"),
                        )
                    except IntegrityError as e:
                        detail = str(e.__cause__) if e.__cause__ else str(e)
                        print(detail)
                        return Response(
                            {
                                "status": "error",
                                "message": f"Bible verse registration fail. Try again.{detail}",
                            },
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                    except Exception as e:
                        return Response(
                            {
                                "status": "error",
                                "message": f"An error occurred while processing your request. {str(e)}",
                            },
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR,)

                    print(instance.id)
                    print(data)

                response = {
                    "status": "success",
                    "message": "Bible verses created successfully",
                }
                return Response(data=response, status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": f"An error occurred while processing your request. {str(e)}",
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

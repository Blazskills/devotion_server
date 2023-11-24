from django.urls import path

from . import views

urlpatterns = [
    path("TestApi/", views.TestApi.as_view(), name="TestApi"),
    path("month/list/<str:month>/", views.MonthListView.as_view(), name="month_list"),
    path("bible/verses/list/<str:month>/<str:day>/", views.BibleVersesListView.as_view(), name="month_verses"),
    path("month/bible/verses/create/", views.BibleVersesMonthCreate.as_view(), name="month_verses_create"),
]

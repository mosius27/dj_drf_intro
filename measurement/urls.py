from django.urls import path
from .views import SensorList, SensorDetail, MeasurementList, MeasurementDetail


urlpatterns = [
    path('sensors/', SensorList.as_view()),
    path('sensors/<int:pk>/', SensorDetail.as_view()),
    path('measurements/', MeasurementList.as_view()),
    path('measurements/<int:pk>/', MeasurementDetail.as_view()),
]

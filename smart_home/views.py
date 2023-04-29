from rest_framework.generics import CreateAPIView
from .serializers import MeasurementSerializer
from .models import Measurement


class MeasurementCreateAPIView(CreateAPIView):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()
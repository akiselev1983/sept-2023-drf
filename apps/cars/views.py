from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .filters import cars_filter




class CarListCreateView(ListCreateAPIView):

    serializer_class = CarSerializer

    def get_queryset(self):
        return cars_filter(self.request.query_params.dict())


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    queryset = CarModel.objects.all()
    serializer_class = CarSerializer











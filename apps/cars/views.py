from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from core.pagination import PagePagination

from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer

from .filters import cars_filter


class CarListView(ListAPIView):

    serializer_class = CarSerializer

    queryset = CarModel.objects.all()

    # def get_queryset(self):
    #     return cars_filter(self.request.query_params.dict())


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    queryset = CarModel.objects.all()
    serializer_class = CarSerializer




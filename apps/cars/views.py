from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .filters import cars_filter


# class CarListCreateView(GenericAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         # cars = CarModel.objects.all().filter(brand='bmw')
#         # cars = CarModel.objects.all().filter(year__range=(2000, 2010)).order_by('year')
#         # cars = CarModel.objects.all().order_by('-year', '-id')
#         #qs = cars_filter(self.request.query_params.dict())
#         qs = self.get_queryset()
#         serializer = self.get_serializer(qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = self.get_serializer(data=data)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class CarRetrieveUpdateDestroyView(GenericAPIView):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, *args, **kwargs):
#         car = self.get_object()
#         # pk = kwargs['pk']
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     #return Response('not found', status.HTTP_404_NOT_FOUND)
#         #     raise Http404()
#         #car = get_object_or_404(CarModel, pk=pk)
#         serializer = CarSerializer(car)
#
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         #pk = kwargs['pk']
#         data = self.request.data
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     #return Response('not found', status.HTTP_404_NOT_FOUND)
#         #     raise Http404()
#         car = self.get_object()
#         serializer = self.get_serializer(car, data)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         #pk = kwargs['pk']
#         data = self.request.data
#
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     #return Response('not found', status.HTTP_404_NOT_FOUND)
#         #     raise Http404()
#         car = self.get_object()
#         serializer = self.get_serializer(car, data, partial=True)
#
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         # try:
#         #     CarModel.objects.get(pk=pk).delete()
#         # except CarModel.DoesNotExist:
#         #     #return Response('not found', status.HTTP_404_NOT_FOUND)
#         #     raise Http404()
#         self.get_object().delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CarListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#
# class CarRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = CarModel.objects.all()
#     serializer_class = CarSerializer
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)



class CarListCreateView(ListCreateAPIView):
    #queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return cars_filter(self.request.query_params.dict())


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer











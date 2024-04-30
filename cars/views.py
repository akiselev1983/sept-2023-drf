from rest_framework.views import APIView
from rest_framework.response import Response
from cars.models import CarModel

# class CarTestView(APIView):
#
#     def get(self, *args, **kwargs):
#         return Response('Hello World get')
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         params_dict = self.request.query_params.dict()
#         print(data)
#         print(params_dict)
#         return Response('Hello World post')
#
#     def put(self, *args, **kwargs):
#         return Response('Hello World put')
#
#     def patch(self, *args, **kwargs):
#         return Response('Hello World patch')
#
#
#     def delete(self, *args, **kwargs):
#         return Response('Hello World delete')
#
# class CarDetailView(APIView):
#     def get(self, *args, **kwargs):
#         print(kwargs)
#         return Response('Hello World get')

class CarListCreateView(APIView):

    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        res = [{'id':car.pk, 'brand':car.brand, 'price':car.price, 'year':car.year} for car in cars]
        return Response(res)
    def post(self, *args, **kwargs):
        data = self.request.data
        CarModel.objects.create(**data)
        return Response('created')
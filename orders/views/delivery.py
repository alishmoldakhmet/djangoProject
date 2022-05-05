from django.shortcuts import get_object_or_404
from rest_framework import viewsets,permissions
from rest_framework.response import Response
from ..models import Delivery
from rest_framework.decorators import action,permission_classes
from ..serializers import DeliveryDetial,OrderList
from drf_yasg.utils import swagger_auto_schema


class DeliveryViewSet(viewsets.ViewSet):

    queryset = Delivery.objects.all()


    def retrieve(self,request,id,*args, **kwargs):
        data = get_object_or_404(Delivery,id=id)
        serializer = DeliveryDetial(data)
        return Response(serializer.data)

    def list(self,request,*args,**kwargs):
        data = Delivery.objects.filter(user=request.user)
        serializer = OrderList(data,many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=DeliveryDetial,responses={200:DeliveryDetial}
    )
    def create(self,request,*args,**kwargs):
        serializer = DeliveryDetial(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data)


    def destroy(self,request,id,*args,**kwargs):
        instance = get_object_or_404(Delivery,id=id)
        instance.canceled=True
        return Response()
    

    @action(detail=False,methods=['GET'])
    @permission_classes([permissions.IsAuthenticated,permissions.IsAdminUser])
    @swagger_auto_schema(responses={200:DeliveryDetial(many=True)})
    def get_orders(self,request):
        store = request.user.store
        data = Delivery.objects.filter_store_Order(store_id=store.id)
        serializer = DeliveryDetial(data,many=True)
        return Response(serializer.data)
    
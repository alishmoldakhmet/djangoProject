from django.shortcuts import get_object_or_404
from rest_framework import viewsets,permissions
from rest_framework.response import Response
from ..models import Order
from rest_framework.decorators import action,permission_classes
from ..serializers import OrderDetial,OrderList


class OrderViewSet(viewsets.ViewSet):

    queryset = Order.objects.all()


    def retrieve(self,request,id,*args, **kwargs):
        data = get_object_or_404(Order,id=id)
        serializer = OrderDetial(data)
        return Response(serializer.data)

    def list(self,request,*args,**kwargs):
        data = Order.objects.filter(user=request.user)
        serializer = OrderList(data,many=True)
        return Response(serializer.data)

    def create(self,request,*args,**kwargs):
        serializer = OrderDetial(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data)


    def destroy(self,request,id,*args,**kwargs):
        instance = get_object_or_404(Order,id=id)
        instance.canceled=True
        return Response()
    

    @action(detail=False,methods=['GET'])
    @permission_classes([permissions.IsAuthenticated,permissions.IsAdminUser])
    def get_orders(self,request):
        store = request.user.store
        data = Order.objects.filter_store_Order(store_id=store.id)
        serializer = OrderDetial(data,many=True)
        return Response(serializer.data)
    
from .serializers import NameSerializer
from .models import Category,Products
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action,permission_classes
from rest_framework.renderers import JSONRenderer
from django.shortcuts import get_object_or_404
from .serializers import ProductDetailSerializer, ProductListSerializer

class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        data = Category.objects.all()
        serializer = NameSerializer(data,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        data = get_object_or_404(Category,id=pk).products.all()
        serializer = ProductListSerializer(data,many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ViewSet):


    def list(self,request):
        data = Products.objects.all()
        serializer = ProductListSerializer(data,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk):
        data = get_object_or_404(Products,pk=pk)
        serializer = ProductDetailSerializer(data)
        return Response(serializer.data)
    

    def create(self,request):
        store = get_object_or_404(user=request.user)
        serializer = ProductDetailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(store=store)
        return Response(serializer.data)
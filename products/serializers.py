from rest_framework import serializers
from .models import Products

class NameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ("id","name")


class ProductDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name",read_only=True)

    class Meta:
        model = Products
        fields = ('id','name','description','price','category_name','category',)
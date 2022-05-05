from rest_framework import serializers
from .models import DelItems, Order,Items,Delivery

class OrderList(serializers.Serializer):

    id = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    address = serializers.CharField(required=False)
    is_finished = serializers.BooleanField(required=False,read_only=True)
    paid = serializers.BooleanField(read_only=True)
    total = serializers.SerializerMethodField(read_only=True)

    def get_total(self,obj):
        return obj.get_total_cost()


class ItemsSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(source="product.name",read_only=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Items
        fields = ('product','product_name','price','quantity','total')

        extra_kwargs = {
            'price': {'read_only':True,}
        }
    
    def get_total(self,obj):
        return obj.get_cost()
    


class OrderDetial(serializers.ModelSerializer):

    items = ItemsSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('items','created_at','paid','total')

    def get_total(self,obj):
        return obj.get_total_cost()
    

    def create(self,validated_data):
        items = validated_data.pop('items')
        instance = Order.objects.create(**validated_data)
        for item in items:
            item['price'] = item['product'].price
            Items.objects.create(**item,order=instance)
        return instance


class DeliveryDetial(serializers.ModelSerializer):

    items = ItemsSerializer(many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Delivery
        fields = ('items','created_at','paid','total','is_finished')

    def get_total(self,obj):
        return obj.get_total_cost()
    

    def create(self,validated_data):
        items = validated_data.pop('items')
        instance = Delivery.objects.create(**validated_data)
        for item in items:
            item['price'] = item['product'].price
            DelItems.objects.create(**item,delivery=instance)
        return instance
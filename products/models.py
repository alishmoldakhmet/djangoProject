from django.db import models
from core.models import AbstractModel

class ProductManager(models.Manager):

    def filter_by_price_desc(self,id_list):
        return self.filter(category__id__in=id_list).order_by("price").desc()
    
    def filter_by_price(self):
        return self.get_queryset().order_by("price")
    

class CategoryManager(models.Manager):

    def get_products(self,id):
        return self.filter(id=id).values_list("products",flat=True)

class Category(AbstractModel):
    pass

    objects = CategoryManager()


class Products(AbstractModel):
    category = models.ForeignKey("products.Category",on_delete=models.SET_NULL,related_name="products",null=True)
    price = models.IntegerField()
    description = models.TextField(null=True)
    objects = ProductManager()
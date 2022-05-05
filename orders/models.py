from django.db import models

class OrderManager(models.Manager):

    def filter_by_date(self,date):
        orders = super().get_queryset().order_by(created_at=date)
        return orders

class Order(models.Model):
    user = models.ForeignKey("users.User",related_name="orders",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)

    objects = OrderManager()

    def get_total_cost(self):
        total = sum( item.get_cost() for item in self.items.all())
        return total

class Items(models.Model):
    order = models.ForeignKey("orders.Order",on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey("products.Products",related_name="orders",on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()


    def get_cost(self):
        return self.price * self.quantity
    

class Delivery(models.Model):
    user = models.ForeignKey("users.User",related_name="deliveries",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    address = models.TextField()
    is_finished = models.BooleanField(default=False)

    def get_total_cost(self):
        total = sum( item.get_cost() for item in self.items.all())
        return total


class DelItems(models.Model):
    delivery = models.ForeignKey("orders.Delivery",on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey("products.Products",related_name="deliveries",on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()


    def get_cost(self):
        return self.price * self.quantity
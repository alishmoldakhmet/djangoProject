from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    favourites = models.ManyToManyField("products.Products",related_name="user")
    phone_number = models.CharField(max_length=18)
    image = models.ImageField(upload_to='users/',null=True)
    first_name = None
    last_name = None
    full_name = models.CharField(max_length=100)
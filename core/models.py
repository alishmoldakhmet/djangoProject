from django.db import models

class AbstractModel(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        abstract = True
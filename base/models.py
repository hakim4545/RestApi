from django.db import models

# Create your models here.
class Item (models.Model):
    name= models.CharField(max_Length=200)
    created = models.DataTimeField(auto_new_add=True)

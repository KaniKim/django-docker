from django.db import models

class ListModel(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.CharField(max_length=255)
    delivery_price = models.IntegerField()
    
    class Meta:
        app_label = "list"

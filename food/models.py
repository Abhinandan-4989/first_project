from django.db import models

# Create your models here.
class Item(models.Model):
    
    def __str__(self):
        return self.item_name
        
    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_images = models.CharField(max_length=500, default="https://cdn.vectorstock.com/i/1000x1000/37/07/fresh-vegetables-with-placeholder-for-text-vector-6263707.webp")
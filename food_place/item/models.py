from django.db import models

# Create your models here.


class Item(models.Model):
        name = models.CharField(max_length=150)
        type = models.CharField(max_length=150)
        description = models.TextField
        price = models.DecimalField(max_digits=10, decimal_places=2)
        image = models.ImageField(upload_to='media/%y/%m/%d/')
        is_available = models.BooleanField(default=False)

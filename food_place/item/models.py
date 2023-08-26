from django.db import models
from django.utils.text import slugify


# Create your models here.


# class Item create for main information of products
class Items(models.Model):
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

# upload_to create name-based path to images
    def upload_to(instance, filename):
        return f"media/{instance.type}/{filename}"

    image = models.ImageField(upload_to=upload_to, blank=True)

    is_available = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)
    seller = models.TextField(blank=True)

# auto-creating slug and description for products
    def save(self, *args, **kwargs):
        if not self.description:
            self.description = f"This is a {self.type} named {self.name}."
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

#name for admin panel
    def __str__(self):
        return self.name

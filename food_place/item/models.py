from django.db import models
from django.utils.text import slugify


# Create your models here.





class Item(models.Model):
        name = models.CharField(max_length=150)
        type = models.CharField(max_length=150)
        description = models.TextField(blank=True)
        price = models.DecimalField(max_digits=10, decimal_places=2)

        def upload_to(instance, filename):
                return f"media/{instance.type}/{filename}"

        image = models.ImageField(upload_to=upload_to)


        is_available = models.BooleanField(default=False)
        slug = models.SlugField(unique=True)

        def save(self, *args, **kwargs):
                if not self.description:
                        self.description = f"This is a {self.type} named {self.name}."
                self.slug = slugify(self.name)
                super().save(*args, **kwargs)


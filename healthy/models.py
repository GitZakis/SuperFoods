from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(null=True)
    category = models.ForeignKey('Categories', null=True, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey('Manufacturers', null=True, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Categories(models.Model):
    title_c= models.CharField(max_length=100)
    description_c = models.TextField()
    image_c = models.ImageField(null=True)

    def __str__(self):
        return self.title_c

class Manufacturers(models.Model):
    title_m = models.CharField(max_length=100)
    description_m = models.TextField()
    image_m = models.ImageField(null=True)

    def __str__(self):
        return self.title_m


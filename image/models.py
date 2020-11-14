from django.db import models
from cloudinary.models import CloudinaryField
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True,null=True)

    class Meta:
        ordering=['name']

    def __str__(self):
        return self.name

    



class Location(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name 





class Image(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=100,null=True)
    description = models.TextField(null=True)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE,null=True)

    class Meta:
        ordering=['title']


    def __str__(self):
        return self.title


    
    


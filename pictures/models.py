from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering=['-name']

    def __str__(self):
        return self.name



class Location(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name 





class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        ordering=['-name']


    def __str__(self):
        return self.name
    


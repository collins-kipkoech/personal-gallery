from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
   

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Location(models.Model):
    name = models.CharField(max_length=60,db_index=True)
     slug = models.SlugField(unique=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('images:images_by_location',args=[self.slug,])



class Image(models.Model):
    
    image_title = models.CharField(max_length=60)
    image_description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return self.image_title

    
    class Meta:
        ordering = ['image_title']

    def get_absolute_url(self):
        return reverse('images:images_details',args=[self.id,])
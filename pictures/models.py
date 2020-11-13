from django.db import models

# Create your models here.
from django.db import models
from cloudinary.models import CloudinaryField

class Image(models.Model):
  image = CloudinaryField('image')
  image_name = models.CharField(max_length =60)
  image_description = models.TextField()
  image_location = models.ForeignKey(Location)
  image_category = models.ForeignKey(Category)

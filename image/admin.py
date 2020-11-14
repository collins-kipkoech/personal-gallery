from django.contrib import admin
from .models import Category,Location,Image

# Register your models here.
admin.site.Register(Category)
admin.site.Register(Location)
admin.site.Register(Image)
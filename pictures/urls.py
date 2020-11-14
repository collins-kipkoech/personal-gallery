from django.urls import path

from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('<slug:category_slug>',views.index,name='images_by_category'),
    path('<int:id>/',views.image_details,name='image_details'),
    path('upload/',views.upload_image,name='upload_image'),
    
]
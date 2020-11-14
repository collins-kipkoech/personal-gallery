from django.urls import path

from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('<slug:location_slug>',views.index,name='images_by_location'),
    path('<int:id>/',views.image_details,name='image_details'),
]
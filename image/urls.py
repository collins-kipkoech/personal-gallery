from django.urls import path

from . import views

app_name = 'image'

urlpatterns =[
    path('',views.index,name='images_list'),
    path('<slug:location_slug>',views.index,name='images_by_location'),
    path('<int:id>/',views.image_details,name='image_details'),
]
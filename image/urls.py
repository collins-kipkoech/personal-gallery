from django.urls import path

from . import views

app_name = 'image'

urlpatterns =[
    path('',views.index,name='images_list'),
    path('<slug:location_slug>',views.index,name='images_by_location'),
    path('search_category/',views.search_category,name='search_category'),
    path('image/',views.single,name='single'),
    
]
from django.shortcuts import render,get_object_or_404
from .models import Category,Location,Image

# Create your views here.
def index(request,location_slug=None):
    location = None
    locations = Location.objects.all()
    images = Image.objects.all()

    if location_slug:
        location = get_object_or_404(Location,slug=location_slug)
        images = images.filter(location=location)

    
    return render(request,'index.html',{'locations':locations,location:location,'images':images})


# def image_details(request,id):
#     images = get_object_or_404(Image,id=id)
#     return render(request,'image_details.html',{'images':images})


def search_category(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        category = Category.objects.all().filter(name=search)
        return render(request,'search.html',{'category':category})
        
    




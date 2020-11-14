from django.shortcuts import render,redirect,get_object_or_404
from .models import Image,Category,Location
from .forms import ImageForm

# Create your views here.
def index(request,category_slug=None):
    category = None
    category = Category.objects.all()
    image = Image.objects.all()
    if category_slug:
        category = get_object_or_404(Category,category=category_slug)
        image = image.filter(category=category)
    return render(request,'index.html',{'categories':categories,'category':category,'image':image,})


def image_details(request,id):
    image = get_object_or_404(Image,id=id)
    return render(request,'image_details.html',{'image':image})



def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('index')
    form = ImageForm()
    return render(request,'upload.html',{'form':form})

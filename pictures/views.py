from django.shortcuts import render
from .models import Image
from .forms import ImageForm

# Create your views here.
def index(request):
    images = Image.objects.all()
    return render(request,'index.html',{'images':images})


def upload_image(request):
    form = ImageForm()
    return render(request,'upload.html',{'form':form})

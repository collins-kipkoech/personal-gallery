from django.shortcuts import render,redirect
from .models import Image
from .forms import ImageForm

# Create your views here.
def index(request):
    images = Image.objects.all()
    return render(request,'index.html',{'images':images})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('index')
    form = ImageForm()
    return render(request,'upload.html',{'form':form})

from django.shortcuts import render
from .models import Category, photos
# Create your views here.
def gallery(request):
    categories = Category.objects.all()
    images = photos.objects.all()
    context = {'categories': categories, 'images': images}
    return render(request, 'photos/gallery.html', context)

def viewphoto(request, pk):
    img = photos.objects.get(id=pk)
    return render(request, 'photos/photo.html',{'img': img})

def addphoto(request):
    return render(request, 'photos/add.html')
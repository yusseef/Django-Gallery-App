from django.shortcuts import render, redirect
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
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.get('img')
        if data['category'] != 'none':
            print(data['category'], 'asdasd')
            category = Category.objects.get(id=data['category'])
            
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None
        photo = photos.objects.create(
            category = category,
            description = data['description'],
            img = images,
        )
        
        return redirect('gallery')
    context = {'categories': categories}
    return render(request, 'photos/add.html', context)
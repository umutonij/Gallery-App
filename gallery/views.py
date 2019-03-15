from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image
# Create your views here.
def gallery(request):
    all_pics = Image.all_pics()
    print(all_pics)
    return render(request, 'gallery.html')

def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_input = request.GET.get('image')
        searched_images = Image.search_by_category(search_input)
        message = f"{search_input}"

        return render(request, 'search.html', {"message":message, "images":searched_images})

    else:
        message = "Please input something in the search field"
        return render(request, 'search.html', {'message':message})

def display_images_categories(request):    
    pics = Image.pic_categories()

    return render(request, 'category.html', {"pics":pics}) 

def display_images_locations(request):    
    pics = Image.pic_locations()

    return render(request, 'location.html', {"pics":pics}) 

from django.shortcuts import render
from cafeteria.models import coffe
from cafeteria.form import coffeForm

def coffe_view(request):
    coffes = coffe.objects.all().order_by('title')
    search = request.GET.get('search')
    if search:
        coffes = coffe.objects.filter(title__icontains=search)

    return render (request, 'index.html', {'coffe': coffes })

def new_coffe_view(request):
    new_coffe_form = coffeForm()
    return render (request, 'new_coffe.html', {'new_coffe_form': new_coffe_form })
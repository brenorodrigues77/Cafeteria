from django.shortcuts import render

def coffe_view(request):
    return render (request, 'index.html', {'coffe': {'title': 'cafe simples'}})

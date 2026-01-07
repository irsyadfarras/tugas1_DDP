from django.shortcuts import render

def home(request):
    return render(request, 'webku/home.html')

def about(request):
    return render(request, 'webku/about.html')

def gallery(request):
    return render(request, 'webku/gallery.html')
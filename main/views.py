from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.defaulttags import lorem

def index(request):
    context = {
        'title': 'Home',
        'content': "Equipment store"
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
            'title': 'About',
            'content': "About us",
            'text_on_page': "Lorem ipsum dolor sit amet consectetur adipisicing elit!"
        }

    return render(request, 'main/about.html', context)
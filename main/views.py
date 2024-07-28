from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.defaulttags import lorem

from goods.models import Categories

def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home',
        'content': "Equipment store",
        'categories': categories
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
            'title': 'About',
            'content': "About us",
            'text_on_page': "Lorem ipsum dolor sit amet consectetur adipisicing elit!"
        }

    return render(request, 'main/about.html', context)
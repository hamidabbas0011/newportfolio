from django.shortcuts import render
from .models import *
# Create your views here.
def homepage(r):
    return render(r, "home.html")

def category(r):
    return render(r, "filter.html",{
        'product': Product.objects.all(),
        "category":Category.objects.all(),
    })

def filter(r):
    pass

def contact(r):
    pass

def viewCard(r):
    pass

def about(r):
    pass
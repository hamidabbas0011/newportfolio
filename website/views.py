from django.shortcuts import render
from .models import *

# Create your views here.


def homepage(r):
    return render(r, "home.html")


def category(r, id=None,filter_id=None):
    all_cats = Category.objects.all()
    all_filter = Filter.objects.filter(category_id=id)
    if id==None:
        products = Product.objects.all()
    else:
        if filter_id == None:
            products = Product.objects.filter(category=id)
        else:
            products = Product.objects.filter(category=id,filter=filter_id)
    return render(r, "filter.html", {
        "category": all_cats,
        "product": products,
        "filters": all_filter
    })




def contact(r):
    pass


def viewCard(r, id):
    data = {"product": Product.objects.get(pk=id)}
    return render(r, "view.html", data)


def about(r):
    pass
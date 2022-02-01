from django.contrib import admin
from .models import *


class CategoryCustom(admin.ModelAdmin):
    list_display = ("cat_id","cat_title")

admin.site.register(Category,CategoryCustom)

class ProductCustom(admin.ModelAdmin):
    list_display = ("pro_id","name","category")

admin.site.register(Product,ProductCustom)
# Register your models here.

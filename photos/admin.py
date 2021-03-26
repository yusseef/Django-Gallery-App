from django.contrib import admin

# Register your models here.
from .models import Category, photos

admin.site.register(Category)
admin.site.register(photos)
from django.contrib import admin

# Register your models here.
from .models import Products

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_url', 'type', 'description', 'brand', 'price', 'available')
    search_fields = ('name', 'type', 'brand', 'price')

admin.site.register(Products, ProductAdmin)
    

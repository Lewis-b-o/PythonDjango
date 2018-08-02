from django.contrib import admin
from .models import Category, Product


# Register your models here.
# Creating new class with type admin.model


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'stock', 'price', 'available', 'image']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}
    list_per_page = 20


admin.site.register(Product, ProductAdmin)
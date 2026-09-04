from django.contrib import admin
from .models import Brand, Category, Product


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'is_active',
        'description',
        
    )

    list_filter = (
        'is_active',
      
    )

    search_fields = (
        'name',
        'description',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'is_active',
        'description',
        
    )

    list_filter = (
        'is_active',
        
    )

    search_fields = (
        'name',
        'description',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'brand',
        'category',
        'is_active',
        'price',
        'description',
        
    )

    list_filter = (
        'is_active',
        'brand',
        'category',
       
    )

    search_fields = (
        'name',
        'description',
       
    )
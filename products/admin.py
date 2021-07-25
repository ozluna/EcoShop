from django.contrib import admin
from .models import Product, Category, ProductReview

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_diplay = (

        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview)



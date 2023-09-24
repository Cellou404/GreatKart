from django.contrib import admin
from .models import Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'is_available', 'category', 'modified_date', 'created_date')
    list_display_links = ('name',)
    list_per_page = 25
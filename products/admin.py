from django.contrib import admin

from .models import Products

# Register your models here.
# admin.site.register(Products)
@admin.register(Products)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'price')
    # list_editable = ('name', 'category')
    list_filter = ('category',)
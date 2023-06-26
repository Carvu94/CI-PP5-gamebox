from django.contrib import admin
from .models import Product, Console

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'console',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)


class ConsoleAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Console, ConsoleAdmin)

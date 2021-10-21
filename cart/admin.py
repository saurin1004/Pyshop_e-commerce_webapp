from django.contrib import admin
from .models import Cart


class CartAdmin(admin.ModelAdmin):
    list_display = ('username', 'productname','quantity','total_price')


admin.site.register(Cart,CartAdmin)

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from order.models import Cart,  CartItem


# Register your models here.
@admin.register(Cart)
class CartAdmin(admin, ModelAdmin):
    list_display = ('id', 'user')


admin.site.register(Cart)
admin.site.register(CartItem)
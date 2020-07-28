from django.contrib import admin
from store import models


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'digital',
    ] 


admin.site.register(models.Customer)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
admin.site.register(models.ShippingAddress)

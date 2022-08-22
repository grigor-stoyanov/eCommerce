from django.contrib import admin

from eCommerce.api.models import Product, Order


class OrderInlineAdmin(admin.TabularInline):
    model = Order.products.through


class ProductInlineAdmin(admin.TabularInline):
    model = Product.order_set.through


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (Product, 'price')
    inlines = (OrderInlineAdmin,)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (Order, 'date',)
    inlines = (ProductInlineAdmin,)
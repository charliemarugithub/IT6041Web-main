from django.contrib import admin
from .models import Products, \
    Customer, \
    Order, \
    OrderItem, \
    ShippingAddress, \
    Staff


# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name',
                    'category',
                    'description',
                    'price',
                    'sku',
                    'stock_level',
                    'image',
                    'popular',
                    'digital',
                    )

    def product_name(self, obj):
        return obj.product_name


class CustomersAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'name',
                    'email',
                    )

    def customer(self, obj):
        return obj.customer


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('customer',
                    'date_ordered',
                    'complete',
                    'transaction_id',
                    )

    def order(self, obj):
        return obj.order


class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('product',
                    'order',
                    'quantity',
                    'date_added',
                    )

    def orderitem(self, obj):
        return obj.orderitem


class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer',
                    'order',
                    'address',
                    'city',
                    'post_code',
                    'country',
                    )

    def shippingitem(self, obj):
        return obj.shippingitem


class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_full_name',
                    'work_email',
                    'work_phone',
                    'mobile_phone',
                    'department_role',
                    'profile_image',
                    'public_display',
                    )

    def staff(self, obj):
        return obj.staff_full_name


admin.site.register(Products, ProductsAdmin)
admin.site.register(Customer, CustomersAdmin)
admin.site.register(Order, OrdersAdmin)
admin.site.register(OrderItem, OrderItemsAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(Staff, StaffAdmin)

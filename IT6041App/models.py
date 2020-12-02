from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Products(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    sku = models.CharField(max_length=20)
    stock_level = models.IntegerField()
    no_of_sales = models.IntegerField(default='0', null=True, blank=True)
    popular = models.BooleanField(default=False, null=True, blank=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    carousel_listing = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('product_name',)

    def __str__(self):
        return str(self.id)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url



class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

        @property
        def coupon(self):
            if self.coupon_id:
                return Coupon.objects.get(id=self.coupon_id)
        return None

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal('100')) * self.get_cart_total()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_cart_total() - self.get_discount()

class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order)

    @property
    def get_total(self):
        total = float(self.product.price) * float(self.quantity)
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    post_code = models.CharField(max_length=200, null=False)
    country = models.CharField(default='', null=True, max_length=200)

    def __str__(self):
        return self.address


class Staff(models.Model):
    staff_full_name = models.CharField(max_length=200)
    work_email = models.EmailField(max_length=200)
    work_phone = models.CharField(max_length=20)
    mobile_phone = models.CharField(max_length=20)
    department_role = models.CharField(max_length=200)
    profile_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    public_display = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Staff Members'
        ordering = ('-staff_full_name',)

    def __str__(self):
        return str(self.id)

    def save(self):
        super().save()

        img = Image.open(self.profile_image.path)

        if img.height > 300 or img.width > 250:
            output_size = (300, 250)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)






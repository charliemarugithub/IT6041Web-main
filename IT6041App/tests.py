from django.test import TestCase, Client
from .models import *
from django.urls import reverse

client = Client()

#Test all models
# each model will be tested to see if they can be made and updated
#class ProductTest(TestCase):

#class CustomerTest(TestCase):

#class OrderTest(TestCase):

#class OrderItemTest(TestCase):

#class ShippingAddressTest(TestCase):

#class StaffTest(TestCase):

#class VoucherTest(TestCase):


#Test all URLS
# each URL will be checked to see if they can be accessed
class IndexPageTest(TestCase):

    def test_root_url_resolves_to_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        #test to see if the response of accessing the index is
        # status code 200 - OK

class CartPageTest(TestCase):

    def test_cart_url_resolves_to_index_view(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)

class CheckoutPageTest(TestCase):

    def test_checkout_url_resolves_to_index_view(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)

class StaffPageTest(TestCase):

    def test_staff_url_resolves_to_index_view(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
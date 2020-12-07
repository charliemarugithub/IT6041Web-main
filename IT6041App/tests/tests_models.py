from django.test import TestCase

from IT6041App.models import Products, Staff


class ProductsModelTest(TestCase):

    def setUp(self):
        self.product1 = Products.objects.create(
            product_name='Eco Spray',
            category='Accessories',
            description='Eco Spray for your home',
            price=12.95,
            image='default.jpg',
            sku='testingsku',
            stock_level=5,
            no_of_sales=10,
            popular=True,
            digital=True,
            carousel_listing=False
        )

    def test_all_product_info_is_not_none(self):
        self.assertIsNotNone(self.product1)


class StaffModelTest(TestCase):

    def setUp(self):
        self.staff1 = Staff.objects.create(
            staff_full_name='Charlie Maru',
            work_email='charlie@greenworlds.com',
            work_phone='093030303',
            mobile_phone='0273030303',
            department_role='Software Developer',
            profile_image='default.jpg',
            public_display=True

        )

    def test_if_staff_is_not_none(self):
        self.assertIsNotNone(self.staff1)
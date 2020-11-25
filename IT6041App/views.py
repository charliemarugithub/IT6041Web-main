from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder


def index(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Products.objects.filter(popular=True)
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'IT6041App/index.html', context)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'IT6041App/cart.html', context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'IT6041App/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Products.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        print('User is not logged in')

        print('COOKIES:', request.COOKIES)
        name = data['form']['name']
        email = data['form']['email']

        cookieData = cookieCart(request)
        items = cookieData['items']

        customer, created = Customer.objects.get_or_create(
            email=email,
        )
        customer.name = name
        customer.save()

        order = Order.objects.create(
            customer=customer,
            complete=False,
        )

        for item in items:
            product = Products.objects.get(id=item['id'])
            orderItem = OrderItem.objects.create(
                product=product,
                order=order,
                quantity=item['quantity'],
            )

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)


def staff(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    staff = Staff.objects.all()

    products = Products.objects.filter(category='Clothing')
    context = {'products': products, 'cartItems': cartItems, 'staff': staff}
    return render(request, 'IT6041App/staff.html', context)


def privacy(request):
    data = cartData(request)
    cartItems = data['cartItems']
    page_title = 'Privacy Policy'
    return render(request, 'IT6041App/privacy.html', {'page_title': page_title, 'cartItems': cartItems})


def terms(request):
    data = cartData(request)
    cartItems = data['cartItems']
    page_title = 'Terms and Conditions'
    return render(request, 'IT6041App/terms.html', {'page_title': page_title, 'cartItems': cartItems})

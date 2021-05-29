import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from my_app.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'detail.html', {'cart': cart})

def product_cart_bot(request):
    cart = Cart(request)
    products_message = ''
    for product in cart:
        a = Product.objects.get(id=product['id'])
        products_message = products_message + f'{a.title}, {a.price}' + '\n'
    res = requests.get(
        settings.URL+f'{products_message}')
    return Response({
            'success': True,
            'data': 'Order sent'},
            status.HTTP_201_CREATED
        )
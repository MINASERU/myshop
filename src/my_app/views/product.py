from my_app.models import Product, Category, Review
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from rest_framework import filters

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product.html', 
                {
                    'category':category,
                    'categories':categories, 
                    'products':products
                })

def product_detail(request, product_id, slug):
    product = get_object_or_404(Product, id=product_id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    review = Review.objects.filter(product_id = product_id)
    reviews = Review.objects.all()
    return render(request, 'category.html', 
                {
                    'product': product, 
                    'cart_product_form':cart_product_form, 
                    'review': review, 
                    'reviews':reviews
                })


def search(request):
    title = str(request.GET['q'])
    products = Product.objects.filter(title__icontains=title)
    return render(request, 'product.html', {'products':products})

def privacy(request):
    return render(request, 'privacy.html') 

def terms(request):
    return render(request, 'terms.html') 

def about(request):
    return render(request, 'about.html') 
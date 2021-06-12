from django.shortcuts import render, redirect
from my_app.forms import ReviewForm
from my_app.models import Review, Product

def review_create(request, product_id):
    error = ''
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                description = request.POST['description']
                Review.objects.create(description=description, customer_name=request.user.username, product_id=product_id)
                return render(request, 'product.html')
            else:
                error = 'Форма была неверной'

        form = ReviewForm()
        context = {
            'form': form,
            'error': error
        }
        return render(request, 'review_create.html', context)
    return redirect( 'authe:login')

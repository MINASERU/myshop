from django.urls import path
from .views import product_list, product_detail, search, review_create, privacy, terms, about


app_name = 'my_app'

urlpatterns = [
    path('', product_list, name = 'product_list'),
    path('search/', search, name='search_results'),
    path('review/create/<int:product_id>', review_create, name = 'review_create'),
    path('<slug:category_slug>/', product_list, name = 'product_list_by_category'),
    path('<int:product_id>/<str:slug>', product_detail, name = 'product_detail'),
    path('privacy', privacy, name = 'privacy'),
    path('terms', terms, name = 'terms'),
    path('about', about, name = 'about')
]
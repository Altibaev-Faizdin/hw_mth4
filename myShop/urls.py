from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.all_categories, name='categories'),
    path('products/', views.all_products, name='products'),
    path('category/<int:cat_id>/', views.products_by_category, name='category_products'),
]
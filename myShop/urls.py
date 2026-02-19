from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.AllCategoriesView.as_view(), name='categories'),
    path('products/', views.AllProductsView.as_view(), name='products'),
    path('category/<int:cat_id>/', views.ProductsByCategoryView.as_view(), name='category_products'),
]
from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def all_categories(request):
    category_list = Category.objects.all()
    return render(request, 'categories.html', {'categories': category_list})


def all_products(request):
    product_list = Product.objects.select_related('category')
    return render(request, 'products.html', {'products': product_list})


def products_by_category(request, cat_id):
    category_obj = get_object_or_404(Category, id=cat_id)
    items_in_category = category_obj.items.all()
    return render(request, 'category_products.html', {
        'category': category_obj,
        'products': items_in_category
    })


from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views import generic
from django.urls import reverse, reverse_lazy



class AllCategoriesView(generic.ListView):
    template_name = 'categories.html'
    context_object_name = 'categories'
    model = Category


class AllProductsView(generic.ListView):
    template_name = 'products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.select_related('category')


class ProductsByCategoryView(generic.ListView):
    template_name = 'category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['cat_id'])
        return self.category.items.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context




# def all_categories(request):
#     category_list = Category.objects.all()
#     return render(request, 'categories.html', {'categories': category_list})


# def all_products(request):
#     product_list = Product.objects.select_related('category')
#     return render(request, 'products.html', {'products': product_list})


# def products_by_category(request, cat_id):
#     category_obj = get_object_or_404(Category, id=cat_id)
#     items_in_category = category_obj.items.all()
#     return render(request, 'category_products.html', {
#         'category': category_obj,
#         'products': items_in_category
#     })


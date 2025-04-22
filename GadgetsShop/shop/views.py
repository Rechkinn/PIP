from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from shop.models import User, Order, Cart, Product


# def data_view(request):
#     users = User.objects.all()
#     products = Product.objects.all()
#     orders = Order.objects.all()
#
#     dict_data = {
#         'users': users,
#         'products': products,
#         'orders': orders
#     }
#
#     return render(request, 'data.html', dict_data)


class HomePageView(TemplateView):
    template_name = 'home.html'

class CartsListView(ListView):
    template_name = 'carts.html'
    model = Cart
    context_object_name = 'list_of_all_carts'

class UserDetailView(DetailView):
    template_name = 'user_details.html'
    model = User
    context_object_name = 'user_details'

class ProductDetailView(DetailView):
    template_name = "product_details.html"
    model = Product
    context_object_name = "product_details"

class OrderDetailView(DetailView):
    template_name = "order_details.html"
    model = Order
    context_object_name = "order_details"


from django.urls import path
# from .views import HomePageView, ProductListView, BrandListView, CategoryListView
# from .views import HomePageView, property_list
# from .views import data_view
# from .views import UsersListView, HomePageView
# urlpatterns = [
#     path('', HomePageView.as_view(), name='home'),
#     # path('products', ProductListView.as_view(), name='products'),
#     # path('brands', BrandListView.as_view(), name='brands'),
#     # path('categories', CategoryListView.as_view(), name='categories')
#     path('users/', UsersListView.as_view(), name='users'),
#     # path('orders', OrdersListView.as_view(), name='orders'),
#     # path('orders/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
#     # path('properties/', property_list(request=True, ObjectClass=User, ), name='property_list'),
#     path('data/', data_view, name='data'),
# ]

from django.urls import path
from .views import HomePageView, CartsListView, UserDetailView, ProductDetailView, OrderDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # path('users', UsersListView.as_view(), name='users'),
    # path('users/<int:pk>', UserListView.as_view(), name='user_detail'),
    # path('users/<str:pk>', UserListView.as_view(), name='user_detail'),
    # path('orders', OrdersListView.as_view(), name='orders'),
    # path('orders/<int:pk>', OrderDetailView.as_view(), name='order_detail'),

    path('carts', CartsListView.as_view(), name='carts'),
    path('carts/user/<int:pk>', UserDetailView.as_view(), name='user_details'),
    path('carts/product/<int:pk>', ProductDetailView.as_view(), name='product_details'),
    path('carts/order/<int:pk>', OrderDetailView.as_view(), name='order_details'),
]

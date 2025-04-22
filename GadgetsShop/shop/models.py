from django.db import models


class User(models.Model):
    id_user = models.AutoField("ID", primary_key = True)
    email = models.EmailField("E-mail", max_length=256)
    first_name = models.CharField("First Name", max_length=256)
    last_name = models.CharField("Last Name", max_length=256)
    phone_number = models.CharField("Phone Number", max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    # def get_id_user(self):
    #     return self.id_user


# class Administrator(User):
#     # id_admin = models.AutoField("ID", primary_key=True)
#     # def __str__(self):
#     #     return f'{self.first_name} {self.last_name}'
#
#     def manage_users(self):
#         pass
#
#     def manage_orders(self):
#         pass
#
#     def manage_products(self):
#         pass
#
#     def manage_review(self):
#         pass



class Category(models.Model):
    id_category = models.AutoField("ID", primary_key=True)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name



class Brand(models.Model):
    id_brand = models.AutoField("ID", primary_key=True)
    name = models.CharField(max_length=256)
    country = models.CharField(max_length=256)

    def __str__(self):
        return self.name



class Product(models.Model):
    product_id = models.AutoField("ID", primary_key=True)
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField("Price", max_digits=10, decimal_places=2)
    count_storage = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image_url = models.URLField()
    # admin_added = models.ForeignKey(Administrator, on_delete=models.SET_NULL, null=True)
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Favorites(models.Model):
    id_favorites = models.AutoField("ID", primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return f'ID Каталога избранное: {self.id_favorites}'


class Review(models.Model):
    id_review = models.AutoField("ID", primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'ID Отзыва: {self.id_review}'


class Order(models.Model):
    id_order = models.AutoField("ID", primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=256, default='Pending')
    date_created = models.DateTimeField(auto_now_add=True)
    date_delivery = models.DateTimeField(null=True, blank=True)
    payment_method = models.CharField(max_length=256)
    pickup_location = models.CharField(max_length=256)
    total_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    def __str__(self):
        return f'Номер заказа: {self.id_order}'


class Cart(models.Model):
    id_cart = models.AutoField("ID", primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count_product = models.IntegerField(default=1)
    def __str__(self):
        return f'ID Корзины: {self.id_cart}'


from django.db import models
from shop.models import Product


class ShopCart(models.Model):
    c_id = models.CharField(max_length=250, blank=True)
    add = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'ShopCart'
        ordering = ['add']

    def __str__(self):
        return self.c_id


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shoppingcart = models.ForeignKey(ShopCart, on_delete=models.CASCADE)
    item_quantity = models.IntegerField()

    class Meta:
        db_table = 'Item'

    def total(self):
        return self.product.price * self.item_quantity

    def __str__(self):
        return self.product

# Create your models here.

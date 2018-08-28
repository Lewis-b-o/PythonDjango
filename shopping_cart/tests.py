from django.test import TestCase
from .models import Item, ShopCart
from shop.models import Product, Category
from shopping_cart.models import Item
from .views import remove_from_cart
# """ unit testing """
# """ Creating TesCare class to test the calculation of the product price times by the quantity """
class ItemTestCase(TestCase):
    # """ setUp command is used to set up the test environment such as the database for the newly created objects"""
    def setUp(self):
        # """ Creating new objects to be used for the unit tests passing the parameters and values"""
        Product.objects.create(slug='qw', name='Nike', price=10.00, stock=1, category_id='1')
        Product.objects.create(name='Puma', price=20.00, stock=1, category_id='1')
        # """ Getting the name parameter and value and assigning to a variable to be used in the Item object creation"""
        productnike = Product.objects.get(name='Nike')
        productpuma = Product.objects.get(name='Puma')

        # """ Creating blank ShopCart object due to being majority parameter to be passed into the item total method"""
        ShopCart.objects.create()
        shoppingcart = ShopCart.objects.get()
        # """ Creating new Item object with a item_quantiy of 2"""
        Item.objects.create(
            product=productnike,
            shoppingcart=shoppingcart,
            item_quantity=2
        )
        # """ Creating new item object with a new product and item_quantity """
        Item.objects.create(
            product=productpuma,
            shoppingcart=shoppingcart,
            item_quantity=4
        )

    # """ Creating new method to ensure the product 1 is equal to the item total of 20 """
    def test_item_total(self):
        """Total should return correct total"""
        item = Item.objects.get(product=1)
        self.assertEqual(item.total(), 20)

    def test_item_total_change_quantity(self):
        """Total should not return a correct total"""
        item = Item.objects.get(product=2)
        self.assertEqual(item.total(), 80)

    # """ Creating new method to test the negative path to ensure the test successfully rejects incorrect total """
    def test_item_total_not(self):
        """Total should not return correct total"""
        item = Item.objects.get(product=2)
        self.assertNotEqual(item.total(), 130)


class DeleteItemFromCart(TestCase):
    def setUp(self):
        ShopCart.objects.create(c_id=1)
        cat = Category.objects.create(id=1)
        Product.objects.create(id=1, price=10.99, stock=1, category=cat)

        itemid = Product.objects.get(id=1)
        shoppingcarid = ShopCart.objects.get(c_id=1)

        Item.objects.create(
            product=itemid,
            shoppingcart=shoppingcarid,
            item_quantity=1
        )

    def test_cart_item_delete(self):
        """ remove item from cart """

        self.assertRedirects(remove_from_cart(self, product_id=1), '/')



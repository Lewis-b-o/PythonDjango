from django.shortcuts import get_object_or_404, render, redirect
from django.core.exceptions import ObjectDoesNotExist
from . models import ShopCart, Item
from shop.models import Product
# Create your views here.

#Adding session ID's for the user


def _id(request):
    shop_cart = request.session.session_key
    if not shop_cart:
        shop_cart = request.session.create()
    return shop_cart


def _adding_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        shoppingcart = ShopCart.objects.get(c_id=_id(request))
    except ShopCart.DoesNotExist:
        shoppingcart = ShopCart.objects.create(
                c_id=_id(request)
        )
        shoppingcart.save()
    try:
        item_to_cart = Item.objects.get(product=product, shoppingcart=shoppingcart)
        if item_to_cart.item_quantity < item_to_cart.product.stock:
            item_to_cart.item_quantity += 1
            item_to_cart.save()
    except Item.DoesNotExist:
        item_to_cart = Item.objects.create(
            product=product,
            item_quantity=1,
            shoppingcart=shoppingcart
        )
        item_to_cart.save()
    return redirect('shopping_cart:Itemcartdetails')


def Itemcartdetails(request, total=0, counter=0, cart_items=None):
    try:
        shoppingcart = ShopCart.objects.get(c_id=_id(request))
        cart_items = Item.objects.filter(shoppingcart=shoppingcart)
        for c_item in cart_items:
            total += (c_item.product.price * c_item.item_quantity)
            counter += c_item.item_quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'shoppingcart.html', dict(cart_items=cart_items, total=total, counter=counter))


def remove_all_items(request, product_id):
    shoppingcart = ShopCart.objects.get(c_id=_id(request))
    product = get_object_or_404(Product, id=product_id)
    items = Item.objects.get(product=product, shoppingcart=shoppingcart)
    items.delete()
    return redirect('shopping_cart:Itemcartdetails')


def remove_from_cart(request, product_id):
    shoppingcart = ShopCart.objects.get(c_id=_id(request))
    product = get_object_or_404(Product, id=product_id)
    items = Item.objects.get(product=product, shoppingcart=shoppingcart)
    if items.item_quantity > 1:
        items.item_quantity -= 1
        items.save()
    else:
        items.delete()
    return redirect('shopping_cart:Itemcartdetails')
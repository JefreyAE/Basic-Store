from django.shortcuts import render, redirect, get_object_or_404
from home.models import *

def index(request):

    if request.user:
        user = request.user
        pass

    cart, _ = Cart.objects.get_or_create(user_id = user.id)

    items = []
    itemcarts = ItemCart.objects.filter(cart=cart)

    total = 0

    for itemcart in itemcarts:
        item = itemcart.item
        item.quantity = itemcart.quantity
        items.append(item)
        total += item.price * itemcart.quantity

    categories = Category.objects.all()
    topics = Topic.objects.all()

    return render(request, 'cartIndex.html', {"categories": categories, 'topics': topics, 'items': items, 'total': total})

def add(request, id):

    item = get_object_or_404(Item, id=id)

    if request.user:
        user = request.user
        pass

    cart, _ = Cart.objects.get_or_create(user_id = user.id)

    cart_and_item, exist = ItemCart.objects.get_or_create(cart_id=cart.id,item_id=id)
    cart_and_item.quantity += 1
    cart_and_item.save()

    return redirect('cart')

def remove(request, id):

    item = get_object_or_404(Item, id=id)
    if request.user:
        user = request.user
        pass

    cart, _ = Cart.objects.get_or_create(user_id = user.id)
    item = Item.objects.get(id=id)

    cart_and_item, exist = ItemCart.objects.get_or_create(cart_id=cart.id,item_id=item.id)
    cart_and_item.quantity -= 1

    if cart_and_item.quantity == 0:
        return redirect('cartDelete', id=id)
    
    cart_and_item.save()

    categories = Category.objects.all()

    topics = Topic.objects.all()

    return redirect('cart')

def delete(request, id):

    item = get_object_or_404(Item, id=id)

    if request.user:
        user = request.user
        pass

    cart, _ = Cart.objects.get_or_create(user_id = user.id)
    cart_and_item, exist = ItemCart.objects.get_or_create(cart_id=cart.id,item_id=item.id)
    cart_and_item.delete()

    categories = Category.objects.all()
    topics = Topic.objects.all()

    return redirect('cart')
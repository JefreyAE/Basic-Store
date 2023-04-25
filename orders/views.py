from django.shortcuts import render, redirect
from home.models import *

def index(request, id=""):

    if request.user:
        user = request.user
        pass

    if id != "":
        try:
            orders = Order.objects.filter(user_id=user.id)
        except Order.DoesNotExist:
            orders = []
    else:
        orders = Order.objects.all()

    categories = Category.objects.all()
    topics = Topic.objects.all()

    return render(request, 'orderIndex.html', {"categories": categories, 'topics': topics, 'orders': orders, "sidebar": "",})

def register(request, id=""):

    if request.user:
        user = request.user
        pass

    cart, _ = Cart.objects.get_or_create(user_id = user.id)
    order = Order.objects.create(user_id = user.id)
    order.save()

    items = []
    itemcarts = ItemCart.objects.filter(cart=cart)

    for itemcart in itemcarts:
        order_and_item, exist = ItemOrder.objects.get_or_create(order_id=order.id,item_id=itemcart.item_id)
        order_and_item.quantity = itemcart.quantity
        order_and_item.save()
    
    itemcarts.delete()

    return redirect('orders', id=id)

def detail(request, id):

    if request.user:
        user = request.user
        pass

    order = Order.objects.get(id=id)

    items = []
    itemsOrder = ItemOrder.objects.filter(order=order)

    total = 0

    for itemOrder in itemsOrder:
        item = itemOrder.item
        item.quantity = itemOrder.quantity
        items.append(item)
        total += item.price * itemOrder.quantity

    categories = Category.objects.all()
    topics = Topic.objects.all()

    return render(request, 'orderDetail.html', {"categories": categories, 'topics': topics, 'items': items, 'total': total})
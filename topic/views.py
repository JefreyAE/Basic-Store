from django.shortcuts import render, redirect, get_object_or_404
from home.models import *

def index(request, name='Linux'):

    commands = Command.objects.filter(topic__name=name)
    items = Item.objects.filter(topic__name=name)

    categories = Category.objects.all()
    topic = Topic.objects.get(name=name)

    sideBar = ""
    topics = Topic.objects.all()

    return render(request, 'topicIndex.html', {"name": name, "categories": categories, "commands": commands, "sidebar": sideBar, 'topics': topics, 'topic': topic, 'items': items})

def detail(request, id):

    item = get_object_or_404(Item, id=id)

    categories = Category.objects.all()
    topics = Topic.objects.all()

    return render(request, 'topicDetail.html', {"categories": categories, 'topics': topics, 'item': item})
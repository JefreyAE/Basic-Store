from django.shortcuts import render, HttpResponse, redirect
from home.models import Topic, Item

# Create your views here.

def home(request):

    topics = Topic.objects.all()
    items = Item.objects.all()[:9]
    
    return render(request, 'index.html', { 'topics': topics, 'items': items })
    



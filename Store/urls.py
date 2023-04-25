"""BlogDevJunior URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import home.views as HomeViews
import topic.views as TopicViews
import users.views as UsersViews
import chatBot.views as ChatViews
import cart.views as CartViews
import orders.views as OrderViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeViews.home),
    path('home/', HomeViews.home, name='home'),
    path('topic/', TopicViews.index, name='topic'),
    path('user/register', UsersViews.index, name='registerUser'),
    path('user/save', UsersViews.save, name='saveUser'),
    path('user/login', UsersViews.user_login, name='loginUser'),
    path('user/logout', UsersViews.user_logout, name='logoutUser'),
    path('chat/', ChatViews.index, name='chatBot'),
    path('chat/sendQuestion', ChatViews.sendQuestion, name='sendQuestion' ),
    path('topic/detail/<str:id>', TopicViews.detail, name='topicDetail'),
    path('topic/<str:name>', TopicViews.index, name='topic'),
    path('cart/', CartViews.index, name='cart'),
    path('cart/add/<str:id>', CartViews.add, name='cartAdd'),
    path('cart/remove/<str:id>', CartViews.remove, name='cartRemove'),
    path('cart/delete/<str:id>', CartViews.delete, name='cartDelete'),
    path('order/<str:id>', OrderViews.index, name='orders'),
    path('order/register/<str:id>', OrderViews.register, name='orderRegister'),
    path('order/detail/<str:id>', OrderViews.detail, name='orderDetail'),
]

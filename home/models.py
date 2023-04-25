from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories" 
    def __str__(self) -> str:
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"

    def __str__(self) -> str:
        return self.name

class Command(models.Model):
    code = models.CharField(max_length=100, verbose_name="Code")
    description = models.CharField(max_length=100)
    link = models.CharField(max_length=100, default="")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        pass
    def __str__(self) -> str:
        return f"Linea de codigo: {self.code}"
    
class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images', blank=True)

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        pass

    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        pass

class ItemCart(models.Model):
    cart = models.ForeignKey(Cart, null=True, blank=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        pass

class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)
    order_number = models.IntegerField(unique=True)

    class Meta:
        pass

    @staticmethod
    def generate_order_number():
        rango_min = 10000 
        rango_max = 99999  

        while True:
            number = random.randint(rango_min, rango_max)
            if not Order.objects.filter(order_number=number).exists():
                break

        return number    
    
    def save(self, *args, **kwargs):
        if not self.pk:  
            self.order_number = self.generate_order_number()
        super().save(*args, **kwargs)

class ItemOrder(models.Model):
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        pass



# class Linux(Command):
#     class Meta:
#         verbose_name = "Linux"
#         verbose_name_plural = "Linux Commands"



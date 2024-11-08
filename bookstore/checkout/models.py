from django.db import models
from django.contrib.auth.models import User
from store.models import Books

# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length=10,default='')
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=250)
    email=models.EmailField(max_length=100)
    shipping_address=models.TextField(max_length=1500)
    amount_paid=models.IntegerField(default=0)
    date_ordered=models.DateTimeField(auto_now_add=True)
    shipped=models.BooleanField(default=False)
    date_shipped=models.DateTimeField(blank=True,null=True)
    placed=models.BooleanField(default=False)
    email_sent=models.BooleanField(default=False)
    

    def __str__(self):
        return f'Order - {str(self.order_id)}'
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    book_id=models.ForeignKey(Books,on_delete=models.CASCADE,null=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    quantity=models.PositiveBigIntegerField(default=1)
    price=models.IntegerField(default=0)

    def __str__(self):
        return f'Order - {str(self.book_id)}'
    

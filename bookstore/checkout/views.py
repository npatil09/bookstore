from django.shortcuts import render,redirect
import random
import string
from django.http import HttpResponse
from checkout.models import Order,OrderItem
import datetime

from cart.models import Cart
from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def checkout(req):
    username = req.session.get('username')
    context={}
    total_amount=0
    products=Cart.objects.filter(username__username=username)
    for i in products:
        total_amount += i.total_price
    context['products']=products
    context['total_amount'] = total_amount
    print(total_amount)
    return render(req,'checkout/checkout.html',context)

def order(req):
    if req.method == 'POST':
        username = User.objects.get(username = req.session.get('username'))
        firstname = req.POST.get('firstname')
        lastname = req.POST.get('lastname')
        email = req.POST.get('email')
        address = req.POST.get('address') + req.POST.get('pincode')
        fullname = firstname + lastname

        upper =string.ascii_uppercase
        num = string.digits
        all = upper + num
        temp = random.sample(all,10)
        order_id='ORD' + ''.join(temp)
        print(order_id)
        order_details =Order.objects.create(order_id = order_id,username = username,full_name=fullname,email=email,shipping_address=address,date_ordered =datetime)
        order_details.save()

        paypal_transaction_id = req.POST.get('paypal-button-id')
        print(paypal_transaction_id)
        
        if paypal_transaction_id:
            order_id = Order.objects.get(username__username = username,placed = False)
            cart_items = Cart.objects.filter(username__username = username)
            for cart in cart_items:
                OrderItem.objects.create(
                    order = order_id,
                    book_id = cart.book_id,
                    username = username,
                    quantity = cart.quantity,
                    price = cart.price
                )
                cart.delete()
            Order.objects.filter(username__username = username,placed=False).update(placed = True)
            return redirect('success')
        else:
            return HttpResponse('Invalid payment Information')
        
def success(req):
    context = {}
    username = req.session.get('username')
    order_details = Order.objects.get(username__username= username,email_sent =False)
    subject = 'Order Confirmation' + str(order_details.order_id)
    message ='Dear,' + str(order_details.username)+'\n'+'Thank you for your order '+'\n'+'Your Order will be delivered as soon as posible'
    address = order_details.username.email
    print(address)
    try:
        send_mail(subject,message,settings.EMAIL_HOST_USER,[address])
        context['result'] = 'Email sent successfully'
        Order.objects.filter(username__username= username,email_sent =False).update(email_sent=True)
    except Exception as e:
        context['result'] = f'Error sending Email: {e}'

    return render(req,'checkout/order.html')



    


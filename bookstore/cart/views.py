from django.shortcuts import redirect, render
from store.models import Books
from .models import Cart
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cart(request):
    if request.method == "POST":
        bid = request.POST.get('bid')
        username = User.objects.get(username = request.session.get('username'))
        name = Books.objects.get(book_id = bid)
        print(name)
        products = Cart.objects.filter(book_id=name, username__username=username)
        print(products)
        if products:
            for i in products:
                quantity=i.quantity + 1
                total_price=i.price * quantity
            Cart.objects.filter(book_id=bid,username__username =username).update(quantity=quantity,total_price=total_price)
        else:
            products = Books.objects.filter(book_id=bid)   
            
            for p in products:
                price = p.price
                image = p.book_image
                total_price=p.price
                
            mycart = Cart.objects.create(username = username,book_id=name,price=price,book_image = image,total_price=total_price)
            mycart.save()
    return redirect('home')


def showcart(request):
    username = request.session.get('username')
    context = {}
    products = Cart.objects.filter(username__username = username)
    context['products'] = products
    return render(request,'cart/cart.html',context)



def deletefromcart(request): 
    if request.method == "POST":
        book_id = request.POST.get('bid')  # Get the book_id from the POST request
        print(book_id)

        try:
            # Find the cart item with the matching book and user
            products = Cart.objects.get(id=book_id)  # Use book_id
            print('Deleted')

            products.delete()  # Delete the cart item
        except Books.DoesNotExist:
            print("Book not found")
        except Cart.DoesNotExist:
            print("Cart item not found")

    return redirect('showcart')  # Redirect back to the cart page








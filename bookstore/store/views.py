import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponse 
from . models import Books,Review
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


# Create your views here.
@login_required
def home(req):
    context = {}
    buy = Books.objects.all()
    context['t'] = buy
    return render(req,'store/home.html',context)

@login_required
def search(req):
    context = {}
    if req.method == 'POST':  
        bookname = req.POST.get('book_name')  
        bookshop = Books.objects.filter(book_name__contains=bookname)  
        print(bookshop)
        context = {'books': bookshop}
    return render(req, 'store/search.html', context)

def bookworm(req):
    return render(req,'store/bookworm.html')

def profile(req):
    return render(req,'store/profile.html')


def review(request):
    if request.method == "POST":
        book_id = request.POST.get('bid')  # Get the book ID from the button value
        book = get_object_or_404(Books, book_id=book_id)
        context = {'book': book}
        return render(request, 'store/review.html', context)

    return render(request, 'store/review.html')

def book_info(req):
    context = {}
    
    if req.method == 'POST':
        book_id = req.POST.get('book_id')  
        print(book_id)
        if not book_id:
           
            return render(req, 'store/book_info.html', {'error': 'Invalid book ID'})

        user_name = req.POST.get('user_name')
        review_text = req.POST.get('review_text')

        reviews = Review.objects.filter(book_id=book_id) 
        
      
        book = Books.objects.get( book_id=book_id)
        
        if book and review_text:
            my_review = Review.objects.create(
                book_id=book,  
                user_name=user_name,
                review_text=review_text,
                created_at=datetime.datetime.now()
            )
            
            my_review.save()
        context = {'book': book, 'reviews': reviews}
        
        
        # return redirect('book_info', pk=book_id) 
    
    return render(req, 'store/book_info.html', context)
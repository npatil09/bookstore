from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('search',views.search,name='search'),
    path('bookworm',views.bookworm,name='bookworm'),
    path('profile',views.profile,name='profile'),
    
    path('review', views.review, name='review'),
    path('book_info',views.book_info, name='book_info')
    
]

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        email = request.POST.get('email')
        # print(username,pass1,pass2,email)
        my_user = User.objects.create_user(username,email,pass1)
        my_user.save()
        return redirect('login')
    return render(request,'user/signup.html')


def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(request,username = username,password = pass1)
        print(user)
        if user is not None:
            login(request,user)
            request.session['username'] = username
            return redirect('home')
        else:
            return HttpResponse('Invalid Username or Password')
    return render(request,'user/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')
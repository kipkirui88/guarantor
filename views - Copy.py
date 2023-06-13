from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import User
from .models import Contact, Subscribers, Payment


User = get_user_model()
# Create your views here.


def Register(request):
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password= request.POST['password']
        mobile = request.POST['phone_number']
        amount = request.POST['amount']
        user = User.objects.create_user(first_name = first_name, last_name = last_name, 
        password = password , email = email, mobile=mobile, amount=amount)
        user.save()
        print('user created')
        return redirect('/login')
    return render(request, 'register.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password = password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            print('Wrong Email or Password')
            return redirect('/login')
    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return redirect("/")    
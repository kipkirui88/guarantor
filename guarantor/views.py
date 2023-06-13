from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import User
from .models import Contact, Subscribers, Payment

# Create your views here.
def index(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Subscriber(request):
    if request.method == 'POST':
        email = request.POST['email']
        mail = Subscribers.objects.create(email = email)
        mail.save()
        return redirect('/')
    return render(request, 'index.html')    

def Contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message= request.POST['message']
        contact = Contact.objects.create(name = name , email = email, subject = subject, message = message)
        contact.save()
        print('message sent')
        return redirect('/')
    return render(request, 'contact.html')

def Services(request):
    return render(request, 'services.html')

def Dashboard(request):
    context = {"payments": Payment.objects.all()}
    return render(request, 'dashboard.html', context)

def Register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password= request.POST['password']
        user = User.objects.create(username = username , first_name = first_name, last_name = last_name, 
        password = password , email = email)
        user.save()
        print('user created')
        return redirect('/pay')
    return render(request, 'register.html')

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            print('Wrong Email or Password')
            return redirect('/login')
    return render(request, 'login.html')

def Payments(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        amount = request.POST['amount']
        pay = Payment.objects.create(phone_number=phone_number, amount = amount)
        pay.save()
        print('Payment Completed')
        return redirect('/login') 
    return render(request, 'payment.html')    
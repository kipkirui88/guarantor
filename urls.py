"""guarantor_guard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.About, name='about'),
    path('contact/', views.Contacts, name='contact'),
    path('services/', views.Services, name='services'),
    path('login/', views.Login, name='login'),
    path('admin/', views.Adminlogin, name='admin'),
    path('adminpage/', views.Admin, name='admin'),
    path('register/', views.Register, name='register'),
    path('logout/', views.Logout, name='logout'),
    # path('pay/', views.Payments, name='pay'),
    path('dashboard/', views.Dashboard, name='dashboard'),
]

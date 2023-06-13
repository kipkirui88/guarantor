from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from . models import  Contact, Subscribers, Payment, User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'mobile','amount')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')

class SubscribersAdmin(admin.ModelAdmin):
    list_display = ['email']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id','phone_number', 'amount')

admin.site.register(User, UserAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscribers, SubscribersAdmin)
admin.site.register(Payment, PaymentAdmin)
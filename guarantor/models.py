from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(max_length=200, unique=True, null=True)
    REQUIRED_FIELDS = ['username']

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contact'

class Subscribers(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email  
    class Meta:
        verbose_name_plural = 'Subscribers'          

class Payment(models.Model):
    phone_number = models.IntegerField()
    amount = models.IntegerField()

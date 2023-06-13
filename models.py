from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password must be provided")

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            mobile = mobile,
            **extra_fields
        )  

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff', True)      
        extra_fields.setdefault('is_active', True)      
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)

    def create_superuser(self, email, password, first_name, last_name, mobile, **extra_fields):
        extra_fields.setdefault('is_staff', True)      
        extra_fields.setdefault('is_active', True)      
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)          

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=100)
    amount = models.CharField(max_length=100, null=True)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

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

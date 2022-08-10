
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class UserCustomerManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(_('Email should be provided'))
        email=self.normalize_email(email)
        new_user=self.model(email=email,**extra_fields)
        new_user.set_password(password)
        new_user.save()
        return new_user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('The superuser should be a staff'))
        
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('The superuser should be a active'))
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('This is for superuser only '))
        
        return self.create_superuser(email,password,**extra_fields)
    
    
class User(AbstractUser):
    
    Options={
        ('A','Artist'),
        ('F','Fan')
    }
    Gender={
        ('M','Male'),
        ('F','Female')
    }
    
    Genre={
        ('R&B','R&B'),
        ('G','Gospel'),
        ('H','Hip Hop'),
        ('T','Traditional Song'),
        ('R','Rap')
        
    }
    
    SignUp_as=models.CharField(choices=Options, max_length=100)
    first_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Username=models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    is_active=models.BooleanField(default=True)
    password=models.CharField(max_length=100)
    create_on=models.DateField(auto_now_add=True)
    Date_of_birth=models.DateField()
    gender=models.CharField(choices=Gender,max_length=100)
    genre=models.CharField(choices=Genre,max_length=100)
    
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS= []
    objects=UserCustomerManager()
    
    def __str__(self):
        return f"<User {self.email}"
        
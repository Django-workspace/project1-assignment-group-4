
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class UserCustomerManager(BaseUserManager):  
    def create_user(self,email,SignUp_as,first_Name,Last_Name,Username,Date_of_birth,gender,genre=None,password=None,**extra_fields):
        if not email:
            raise ValueError(_('Email should be provided'))
        user = self.model(
            
            SignUp_as=SignUp_as,
            first_Name=first_Name,
            Last_Name=Last_Name,
            Username=Username,
            Date_of_birth=Date_of_birth,
            gender=gender,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.is_active=True
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=None,SignUp_as=None,first_Name=None,Last_Name=None,Username=None,Date_of_birth=None,gender=None,genre=None,**extra_fields):
        user = self.model(
            password = password,
            email = self.normalize_email(email),
            **extra_fields
        )
        user.staff = True
        user.superuser = True
        user.is_active = True
        user.password=password
        user.set_password(password)
        user.save(using=self._db)
        
        
        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError(_('The superuser should be a staff'))
        
        # if extra_fields.get('is_active') is not True:
        #     raise ValueError(_('The superuser should be a active'))
        
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError(_('This is for superuser only '))
        # return user
        return self.create_user(email,password,**extra_fields)
    
    
class User(AbstractUser):
    
    Options=[
        ('A','Artist'),
        ('F','Fan')
    ]
    Gender=[
        ('M','Male'),
        ('F','Female')
    ]
    
    Genre=[
        ('R&B','R&B'),
        ('G','Gospel'),
        ('H','Hip Hop'),
        ('T','Traditional Song'),
        ('R','Rap')
        
    ]
    
    SignUp_as=models.CharField(choices=Options, max_length=100)
    first_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Username=models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    is_active=models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    superuser = models.BooleanField(default=False)
    password=models.CharField(max_length=100)
    create_on=models.DateField(auto_now_add=True)
    Date_of_birth=models.DateField(null=True)
    gender=models.CharField(choices=Gender,max_length=100)
    genre=models.CharField(choices=Genre,max_length=100)
    
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS= []
    objects=UserCustomerManager()
    
    def __str__(self):
        return f"<User {self.email}"
    
    
    @property
    def get_name(self):
        return self.username
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_superuser(self):
        return self.superuser


from multiprocessing import AuthenticationError
from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model

# from django.db.models import Q


from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode 
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import *

User=get_user_model()
class UserSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(required=True,write_only=True)
    email=serializers.EmailField()
    def validate(self, attrs):
        SignUp_as=attrs.get('SignUp_as')
        if SignUp_as == 'F':
            
            genre=serializers.HiddenField(default='F',read_only=True)
            return genre
        
        return super().validate(attrs)
    class Meta:
        model=User
        fields=['SignUp_as','first_Name','Last_Name','Username','email','create_on','Date_of_birth','gender','genre','password','confirm_password']
        
        extra_kwargs = {
            'password': {'write_only':True},
            'confirm_password':{'write_only':True}
         }
    
    def validate(self, data):
        email = data.get('email', None)
        if email:
            data['Username'] = email
        return data
        
    def validate_email(self,email):
        existing_email=User.objects.filter(email=email).first()
        if existing_email:
            raise serializers.ValidationError("this Email is already exist!!")
        return email
    
    
    def validate(self, attrs):
        password= attrs.get('password')
        confirm_password=attrs.get('confirm_password')
        if password !=confirm_password:
            raise serializers.ValidationError(
                "password and confirm_password does not match"
            )
        return attrs
        
    def create(self, validated_data):
        password= validated_data.pop('password',None)
        confirm_password= validated_data.pop('confirm_password',None)
        instance=User.objects.create(**validated_data)
        if password is not None:
            instance.set_password(password)  
        instance.save()
        return instance
    
class UserSerializerLogIn(serializers.ModelSerializer):
     class Meta:
        model=User
        fields=['id','Username','email','password']
        extra_kwargs = {
            'Username': {'read_only':True},
         }
        
        
# class FogetpasswordSerializer(serializers.ModelSerializer):
    
#     email=serializers.CharField()
#     confirm_password=serializers.CharField(required=True,write_only=True)
    
#     class Meta:
#         model=User
#         fields=['email','password','confirm_password']
        
        
#         extra_kwargs = {
#             'password': {'write_only':True},
#             'confirm_password':{'write_only':True}
#          }
    
#     def validate(self, attrs):
#         password= attrs.get('password')
#         confirm_password=attrs.get('confirm_password')
#         if password !=confirm_password:
#             raise serializers.ValidationError(
#                 "password and confirm_password does not match"
#             )
#         return attrs
    
    # def validate_email(self,email,validated_data):
    #     existing_email=User.objects.filter(email=email).first()
    #     if existing_email:
    #         password= validated_data.pop('password',None)
    #         confirm_password= validated_data.pop('confirm_password',None)
    #         instance=User.objects.update(**validated_data)
    #         if password is not None:
    #             instance.set_password(password)  
    #         instance.save()
    #         return instance
            
    #     raise serializers.ValidationError("this Email isn't exist!!")
        
        
class ResetPassordSerializer(serializers.Serializer):
    email=serializers.CharField(max_length=100)
    
    class Meta:
        fields=['email']
        
        
class SetNewPasswordserializer(serializers.Serializer):
    password=serializers.CharField(min_length=3,max_length=100, write_only=True)
    confirm_password=serializers.CharField(min_length=3,max_length=100, write_only=True)
    token=serializers.CharField(min_length=1, write_only=True)
    uidb64=serializers.CharField(min_length=1, write_only=True)
    class Meta:
        fields=['password','token','uidb64','confirm_password']
    
    def validate(self, attrs):
        try:
            password=attrs.get('password')
            confirm_password=attrs.get('confirm_password')
            token=attrs.get('token')
            uidb64=attrs.get('uidb64')
            if password !=confirm_password:
                raise serializers.ValidationError(
                    "password and confirm_password does not match"
                )
            id=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token():
                raise AuthenticationError('This link is already used',401)
            user.set_password(password)
            user.save()
            
            return attrs
        
        except Exception as e:
            raise AuthenticationError('This link is already used',401)
        return super().validate(attrs)
   
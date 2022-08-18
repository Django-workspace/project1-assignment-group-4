from rest_framework import generics
from .models import *
from django.urls import reverse
from .serializers import *
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
class LC_post(generics.ListCreateAPIView):
    queryset=post.objects.all()
    serializer_class=post_Serializer

class RUD_post(generics.RetrieveUpdateDestroyAPIView):
    queryset=post.objects.all()
    serializer_class=post_Serializer

class LC_comments(generics.ListCreateAPIView):
    queryset=post_comments.objects.all()
    serializer_class=comments_Serializer

class RUD_comments(generics.RetrieveUpdateDestroyAPIView):
    queryset=post_comments.objects.all()
    serializer_class=comments_Serializer

    
# def likeView(request, slug):
#     post = get_object_or_404(post, slug=request.POST.get('post_slug'))
#     if request.user in post.likes.all():
#         post.likes.remove(request.user)
#     else:
#         post.likes.add(request.user)
#     return HttpResponseRedirect(reverse('post_detail', args=[str(slug)]))

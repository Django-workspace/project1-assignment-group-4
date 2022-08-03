from rest_framework import generics
from Artist_app.models import *
from .serializers import *
# Create your views here.

class LC_Artist_channel(generics.ListCreateAPIView):
    queryset=Artist_chanel.objects.all()
    serializer_class=Artist_chanel_Serializer

class RU_Retreive_Artist_channel(generics.UpdateAPIView):
    queryset=Artist_chanel.objects.all()
    serializer_class=Artist_chanel_Serializer

class LC_Event(generics.ListCreateAPIView):
    queryset=Event.objects.all()
    serializer_class=Event_Serializer

class RUD_Event(generics.RetrieveUpdateDestroyAPIView):
    queryset=Event.objects.all()
    serializer_class=Event_Serializer

class LC_comment(generics.ListCreateAPIView):
    queryset=comment.objects.all()
    serializer_class=comment_Serializer

class RUD_comment(generics.RetrieveUpdateDestroyAPIView):
    queryset=comment.objects.all()
    serializer_class=comment_Serializer

class LC_post(generics.ListCreateAPIView):
    queryset=post.objects.all()
    serializer_class=post_Serializer

class RUD_post(generics.RetrieveUpdateDestroyAPIView):
    queryset=post.objects.all()
    serializer_class=post_Serializer

class LC_comments(generics.ListCreateAPIView):
    queryset=comments.objects.all()
    serializer_class=comments_Serializer

class RUD_comments(generics.RetrieveUpdateDestroyAPIView):
    queryset=comments.objects.all()
    serializer_class=comments_Serializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from Artist_app.models import *
from .serializers import *
from Post.models import *
from Post.serializers import *

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

class LC_Event_comment(generics.ListCreateAPIView):
    queryset=Event_comment.objects.all()
    serializer_class= Event_comment_Serializer

class RUD_Event_comment(generics.RetrieveUpdateDestroyAPIView):
    queryset=Event_comment.objects.all()
    serializer_class=Event_comment_Serializer

class LC_album(generics.ListCreateAPIView):
    queryset=Album.objects.all()
    serializer_class=Album_serializer

class RUD_album(generics.RetrieveUpdateDestroyAPIView):
    queryset=Album.objects.all()
    serializer_class=Album_serializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = likeser

    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)

    def create(self, request, pk=None):
        serializer=self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=self.request.user)
        post_id=serializer.data['post']
        post=Event.objects.get(id= post_id)
        return Response(post_Serializer(post).data)

    def update(self,request, pk=None):
        like=get_object_or_404(Like , id=pk)
        post=like.event
        self.check_object_permissions(request, like)
        serializer=LikeUpdateSer(like ,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(Event_Serializer(post).data)
        
    def destroy(self, request, pk=None):
        like=get_object_or_404(Like , id =pk)
        post=like.event
        self.check_object_permissions(request, like)
        like.delete()
        return Response(Event_Serializer(post).data)



    
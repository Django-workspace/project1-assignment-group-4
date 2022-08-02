from rest_framework import serializers
from .models import Artist_chanel, Event, comment
from Post.models import post, comments

class Artist_chanel_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Artist_chanel
        fields='__all__'
class Event_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields='__all__'
class comment_Serializer(serializers.ModelSerializer):
    class Meta:
        model=comment
        fields='__all__'
class post_Serializer(serializers.ModelSerializer):
    class Meta:
        model=post
        fields='__all__'
class comments_Serializer(serializers.ModelSerializer):
    class Meta:
        model=comments
        fields='__all__'



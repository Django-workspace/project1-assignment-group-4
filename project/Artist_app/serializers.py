from rest_framework import serializers
from .models import Album, Artist_chanel, Event, Event_comment, Like


class Artist_chanel_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Artist_chanel
        fields='__all__'
class Event_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields='__all__'
class  Event_comment_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Event_comment
        fields='__all__'
class likeser(serializers.ModelSerializer):
    class meta:
        model=Like
        fields='__all__'
        # read_only_fields=['owner']
    def validate(self, data):
        owner_id=self.context['request'].user.id
        post=data['post']

        like=Like.objects.filter(owner=owner_id,post=post.id)
        if like.exists():
            raise serializers.ValidationError('the user already liked')
        return data

class LikeUpdateSer(serializers.ModelSerializer):
    class Meta():
        model=Like
        fields='__all__'
        read_only_fields=['owner','post']

class Album_serializer(serializers.ModelSerializer):
    class Meta():
        model=Album
        fields='__all__'
        





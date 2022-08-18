from rest_framework import serializers
from Post.models import post, post_comments,comment_likes,post_likes
from Artist_app.serializers import likeser

class post_Serializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    lieks_count=serializers.SerializerMethodField()
    delikes_count=serializers.SerializerMethodField()
    likes=serializers.SerializerMethodField()
    class Meta:
        model=post
        fields='__all__'
    # def get_owner(self, obj):
    #     return GetUserserializer(obj.owner).data

    def get_likes_count(self,obj):
        return obj.likes.filter(like = True).count()

    def get_deslike_count(self, obj):
        return obj.likes.filter(like=False).count()
    def get_likes(self, obj):
        return likeser(obj.likes, many=True).data


class comments_Serializer(serializers.ModelSerializer):
    class Meta:
        model=post_comments
        fields='__all__'

class comment_likeSerialiser(serializers.ModelSerializer):
    class Meta:
        model=comment_likes
        fields='__all__'

class post_likeSerialiser(serializers.ModelSerializer):
    class Meta:
        model=post_likes


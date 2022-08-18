from django.contrib import admin
from .models import Artist_chanel
from Post.models import post,Event_comment , post_likes, Event, post_comments


admin.site.register(Artist_chanel)
admin.site.register(Event)
admin.site.register(post)
admin.site.register(post_comments)
admin.site.register(Event_comment)
admin.site.register(post_likes)
from django.contrib import admin
from .models import Artist_chanel, Event, comment
from Post.models import post, comments


admin.site.register(Artist_chanel)
admin.site.register(Event)
admin.site.register(post)
admin.site.register(comment)
admin.site.register(comments)

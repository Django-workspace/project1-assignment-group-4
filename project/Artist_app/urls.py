from django.urls import path
from .views import *

urlpatterns = [
    path('channel', LC_Artist_channel.as_view()),
    path('upd_channel/<int:pk>/', RU_Retreive_Artist_channel.as_view()),
    path('ls_event',LC_Event.as_view()),
    path('ud_event/<int:pk>/',RUD_Event.as_view()),
    path('ls_comment',LC_comment.as_view()),
    path('ud_comment/<int:pk>/',RUD_comment.as_view()),
    path('ls_post',LC_post.as_view()),
    path('ud_post/<int:pk>/',RUD_post.as_view()),
    path('ls_comments',LC_comments.as_view()),
    path('ud_comments/<int:pk>/',LC_comments.as_view()),

]

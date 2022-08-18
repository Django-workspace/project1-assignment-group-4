from django.urls import path
from .views import *
from Post.views import *
from django.conf import settings
from django.conf.urls.static import static
import Artist_app
from rest_framework import routers 

router = routers.DefaultRouter()

router.register('' ,Artist_app.views.LikeViewSet ,basename='likes')

urlpatterns = router.urls
urlpatterns = [
    path('channel', LC_Artist_channel.as_view()),
    path('upd_channel/<int:pk>/', RU_Retreive_Artist_channel.as_view()),
    path('ls_event',LC_Event.as_view()),
    path('ud_event/<int:pk>/',RUD_Event.as_view()),
    path('ls_comment',LC_Event_comment.as_view()),
    path('ud_comment/<int:pk>/',RUD_Event_comment.as_view()),
    path('ls_post',LC_post.as_view()),
    path('ud_post/<int:pk>/',RUD_post.as_view()),
    path('ls_comments',LC_comments.as_view()),
    path('ud_comments/<int:pk>/',LC_comments.as_view()),
    path('ls_Album', LC_album.as_view()),
    path('RUD_Album/<int:pk>/',RUD_album.as_view())

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
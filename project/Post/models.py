from django.db import models
from Artist_app.models import Artist_chanel,Event, Event_comment

# User=True

class post(models.Model):
    title=models.CharField(max_length=100)
    pics=models.ImageField(null=True, upload_to='post image')
    # liked=models.ManyToManyField(User, default=None, blank=True)
    video=models.FileField(upload_to='post_video', null=True, blank=True)
    content=models.TextField()
    channel=models.ForeignKey(Artist_chanel, related_name="channelPost", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

        
class post_comments(models.Model):
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    # liked=models.ManyToManyField(User, default=None, blank=True)
    posts=models.ForeignKey(post, related_name="postComment", on_delete=models.CASCADE)
    comment_image=models.ImageField(upload_to='comment image', blank=True, null=True)

    def __str__(self):
        return self.content

Like_choises=[
    ('Like','Like'),
    ('Unlike','Unlike')
]

class post_likes(models.Model):
    # likepostuser=models.ForeignKey(User, on_delete=models.CASCADE)
    likepost=models.ForeignKey(post, related_name='post_like', on_delete=models.CASCADE)
    value = models.CharField(choices=Like_choises, max_length=10)
    def __str__(self):
        return str(self.likepost)

class comment_likes(models.Model):
    # likecommentuser=models.ForeignKey(User, on_delete=models.CASCADE)
    likecomment=models.ForeignKey(post_comments, related_name="comment_like", on_delete=models.CASCADE)
    value = models.CharField(choices=Like_choises, max_length=10)
    def __str__(self):
        return str(self.likecomment)


class Event_likes(models.Model):
    # likeEventuser=models.ForeignKey(User, on_delete=models.CASCADE)
    likeEvent=models.ForeignKey(Event, related_name='Event_like', on_delete=models.CASCADE)
    value = models.CharField(choices=Like_choises, max_length=10)
    def __str__(self):
        return str(self.likeEvent)


class Event_comment_likes(models.Model):
    # likecommentuser=models.ForeignKey(User, on_delete=models.CASCADE)
    likecommentEvent=models.ForeignKey(Event_comment, related_name='post_like', on_delete=models.CASCADE)
    value = models.CharField(choices=Like_choises, max_length=10)
    def __str__(self):
        return str(self.likecomment)

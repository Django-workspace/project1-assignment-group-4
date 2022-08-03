from django.db import models
from Artist_app.models import Artist_chanel


class post(models.Model):
    title=models.CharField(max_length=100)
    pics=models.ImageField(null=True, upload_to='post image')
    content=models.TextField()
    channel=models.ForeignKey(Artist_chanel, related_name="channelPost", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
        
class comments(models.Model):
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    posts=models.ForeignKey(post, related_name="postComment", on_delete=models.CASCADE)
    comment_image=models.ImageField(upload_to='comment image', blank=True, null=True)

    def __str__(self):
        return self.content
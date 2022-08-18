from django.db import models


# User=models.NullBooleanField(("null"))
class Artist_chanel(models.Model):
    prof_photo=models.ImageField(null=True, upload_to='profilePictures')
    pictures=models.ImageField(null=True, upload_to='pictures')
    name=models.CharField(null=False, max_length=100)
    
    def __str__(self):
        return self.name

class Event(models.Model):
    pricture=models.ImageField(upload_to='Event_picture', null=True, blank=True)
    title=models.CharField(max_length=100)
    # liked=models.ManyToManyField(User, default=None, blank=True)
    content=models.TextField()
    artist_Relation=models.ForeignKey(Artist_chanel, related_name="channel", on_delete=models.CASCADE)
    videos=models.FileField(upload_to='event_videos',null=True, blank=True)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Event_comment(models.Model):
    content=models.TextField()
    # liked=models.ManyToManyField(User, default=None, blank=True)
    created_on=models.DateTimeField(auto_now_add=True)
    event=models.ForeignKey(Event, related_name='eventComment', on_delete=models.CASCADE)
    comment_image=models.ImageField(upload_to='commentimage', blank=True, null=True)
    
    def __str__(self):
        return self.content

class Like(models.Model):
    # owner=models.ForeignKey(User, related_name="likes", on_delete=models.CASCADE)
    event=models.ForeignKey(Event, related_name="likes", on_delete=models.CASCADE)
    like=models.BooleanField()

class Album(models.Model):
    name=models.CharField(max_length=50, unique=True)
    picture=models.ImageField(upload_to='albumPic', null=False, blank=False)
    songs=models.FileField(upload_to='songs',null=False, blank=False)
    date_created=models.DateField(auto_now_add=True)
    # artist=models.OneToOneField(related_name="Artist", on_delete=models.CASCADE)
    description=models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
    
    




# class Event_likes(models.Model):
#     likeEventuser=models.ManyToManyField(User, related_name='event_like_user')
#     likepost=models.ForeignKey(Event, related_name='event_like', on_delete=models.CASCADE)
    
#     def numer_of_likes(self):
#         return self.likes.count()

# class comment_likes(models.Model):
#     likeeventuser=models.ManyToManyField(User, related_name='post_event_user')
#     likeevent=models.ForeignKey(Event_comment, related_name='event_like', on_delete=models.CASCADE)
#     def numer_of_likes(self):
#         return self.likes.count()
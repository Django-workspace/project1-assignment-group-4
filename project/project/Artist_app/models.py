from django.db import models

class Artist_chanel(models.Model):
    prof_photo=models.ImageField(null=True, upload_to='profilePictures')
    pictures=models.ImageField(null=True, upload_to='pictures')
    name=models.CharField(null=False, max_length=100)
    def __str__(self):
        return self.name
class Event(models.Model):
    pricture=models.ImageField(upload_to='Event_picture', null=True, blank=True)
    title=models.CharField(max_length=100)
    content=models.TextField()
    artist_Relation=models.ForeignKey(Artist_chanel, related_name="channel", on_delete=models.CASCADE)
    videos=models.FileField(upload_to='event_videos',null=True, blank=True)
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class comment(models.Model):
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    event=models.ForeignKey(Event, related_name='eventComment', on_delete=models.CASCADE)
    comment_image=models.ImageField(upload_to='comment image', blank=True, null=True)
    def __str__(self):
        return self.content

    


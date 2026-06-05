from django.db import models

# Create your models here.
class VideoCreation(models.Model):
    
    VIDEO_QUALITY = [

        ('360p', '360p'),

        ('720p', '720p'),

        ('1080', '1080p'),

    ]

    video_title = models.CharField(max_length=250)
    description = models.TextField()
    video_quality = models.CharField(

        max_length=20,

        choices=VIDEO_QUALITY,

        default='CASH'

    )
    date_created = models.DateTimeField(auto_created=True)
    thumbnail = models.URLField(max_length=250, blank=True, null=True)



    
   
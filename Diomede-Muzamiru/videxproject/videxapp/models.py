from django.db import models
import datetime

class VideoCreation(models.Model):
    VIDEO_QUALITY = [
        ('360p', '360p'),
        ('720p', '720p'),
        ('1080p', '1080p'), # Fixed '1080' to '1080p'
    ]

    video_title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    video_quality = models.CharField(
        max_length=20,
        choices=VIDEO_QUALITY,
        default='360p'
    )
    date_created = models.DateField(default=datetime.date.today)
    video_file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
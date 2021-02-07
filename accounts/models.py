from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', default='profilepic.jpg', blank=True)
    image_thumbnail = ImageSpecField(source='photo',
                                     processors=[ResizeToFill(200, 250)],
                                     format='JPEG',
                                     options={'quality': 60})

    def __str__(self):
        return 'Profile for user{}'.format(self.user.username)

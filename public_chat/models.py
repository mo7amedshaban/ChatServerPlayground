from django.db import models
from django.conf import settings


# Create your models here.
class PublicChat(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(unique=False, blank=False, )

    def __str__(self):
        return self.content

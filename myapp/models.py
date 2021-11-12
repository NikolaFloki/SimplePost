from django.db import models
from datetime import datetime


class Posts(models.Model):
    title   = models.CharField(max_length=200)
    text    = models.TextField()
    created = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"    #ovo smo hardkodovali da nam u adminu pise posts posto django sam dodaje s 

    
 
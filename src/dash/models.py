from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dash(models.Model):
    title = models.CharField(max_length=120)
    file = models.FileField(upload_to='upload_location')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

        

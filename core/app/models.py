from django.db import models

class Film(models.Model):
    title = models.CharField(max_length = 50)
    file = models.FileField(upload_to = 'media/')
    picture = models.ImageField(upload_to = 'media/')

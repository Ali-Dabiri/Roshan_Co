from django.db import models

class News_Table(models.Model):
    News_Title = models.CharField(max_length=255)
    News_Content = models.TextField()
    News_Tags = models.CharField(max_length=255)
    News_Source = models.CharField(max_length=255)
    
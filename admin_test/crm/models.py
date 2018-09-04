from django.db import models

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=64)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey('Topic',on_delete=models.CASCADE)
    text = models.CharField(max_length=32)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return self.text + '.......'

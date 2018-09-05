from django.db import models


# Create your models here.

class Publish(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)

    def __str__(self):
        return self.city


class Author(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=64)
    price = models.IntegerField()
    color = models.CharField(max_length=64)
    page_num = models.IntegerField(null=True)

    publisher = models.ForeignKey('Publish')
    author = models.ManyToManyField('Author')

    def __str__(self):
        return self.title


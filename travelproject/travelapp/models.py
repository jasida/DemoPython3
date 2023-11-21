from django.db import models


# Create your models here.


class Teams(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

class Members(models.Model):
    persons = models.CharField(max_length=250)
    image = models.ImageField(upload_to='picss')
    about = models.TextField()
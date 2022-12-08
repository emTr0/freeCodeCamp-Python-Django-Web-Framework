from django.db import models

# Create your models here.


class Product(models.Model):
    '''Products Class'''
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='This is cool!')

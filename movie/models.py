from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100,default = 'default',primary_key=True)
    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField(max_length=100)
    basedir = models.CharField(max_length=150)
    date_created = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.name 

class Movies(models.Model):
    title = models.CharField(max_length=25)
    year = models.CharField(max_length=10)
    actors = models.TextField()
    plot = models.TextField()
    poster = models.CharField(max_length=100,null=True)
    imdbRating = models.CharField(max_length=10)
    imdbID = models.CharField(max_length=15,primary_key=True)
    types = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.ForeignKey(Movies, on_delete=models.CASCADE)
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.title
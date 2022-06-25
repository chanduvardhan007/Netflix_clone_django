from re import T
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICES={
    ('ALL','ALL'),
    ('Kids','Kids')
}
MOVIE_CHOICES={
    ('seasonal','Seasonal'),
    ('single','Single')
}

class CustomUser(AbstractUser):
    profiles=models.ManyToManyField('Profile',blank=True)

class Profile(models.Model):
    name=models.CharField(max_length=225)
    age_limlit=models.CharField(max_length=10,choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4)

class Movie(models.Model):
    title=models.CharField(max_length=225)
    description=models.TextField(blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4)
    type=models.CharField(max_length=10,choices=MOVIE_CHOICES)
    videos=models.ManyToManyField('video')
    flyer=models.ImageField(upload_to='flyers')
    age_limit=models.CharField(max_length=10,choices=AGE_CHOICES)

class Video(models.Model):
    title=models.CharField(max_length=225,blank=True,null=True)
    file=models.FileField(upload_to='movies')


     


from django.db import models
from bson import ObjectId

class User(models.Model):
    _id = models.CharField(max_length=24, default=ObjectId, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class Team(models.Model):
    _id = models.CharField(max_length=24, default=ObjectId, primary_key=True)
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='teams')

class Activity(models.Model):
    _id = models.CharField(max_length=24, default=ObjectId, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Leaderboard(models.Model):
    _id = models.CharField(max_length=24, default=ObjectId, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.IntegerField()

class Workout(models.Model):
    _id = models.CharField(max_length=24, default=ObjectId, primary_key=True)
    name = models.CharField(max_length=100)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.IntegerField()

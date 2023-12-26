from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """ Return the topic here """
    name = models.CharField(max_length=200)

    def __str__(self):
        """ Return the string reprs of Topic """
        return self.name

class Room(models.Model):
    """ The room model representation """
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Return string representation of room name """
        return self.name
    
class Message(models.Model):
    """ The message a user can send """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ The string representation of Message model """
        return self.body[0:50]
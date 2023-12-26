from django.db import models

# Create your models here.
class Room(models.Model):
    """ The room model representation """
    #host =
    #topi =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    # participants =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Return string representation of room name """
        return self.name
from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
    """ Trasform the room python model list into a json object """
    class Meta:
        model = Room
        fields = "__all__"
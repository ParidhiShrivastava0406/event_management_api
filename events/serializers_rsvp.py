from rest_framework import serializers
from .models import RSVP

class RSVPSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = RSVP
        fields = ['id', 'event', 'user', 'status']

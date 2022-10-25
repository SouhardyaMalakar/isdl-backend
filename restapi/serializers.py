from rest_framework import serializers

from restapi.models import Actor, Hall

class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hall
        fields='__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields='__all__'
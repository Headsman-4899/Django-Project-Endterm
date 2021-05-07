from rest_framework import serializers

from .models import Review
from users.serializers import CustomerSerializer
from games_app.serializers import GameSerializer
from games_app.models import Game


class ReviewSerializer(serializers.Serializer):
    title = serializers.CharField()
    comment = serializers.CharField()
    rating = serializers.IntegerField()
    reviewer = CustomerSerializer()
    to_game = GameSerializer()


class ReviewModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

from rest_framework import serializers

from .models import Order
from games_app.serializers import GameSerializer
from users.serializers import CustomerSerializer

        
class OrderSerializer(serializers.ModelSerializer):
    username = CustomerSerializer(read_only=True)
   
    class Meta:
        model = Order
        fields = ['username', 'quantity', 'game_name']

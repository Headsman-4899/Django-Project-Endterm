from rest_framework import serializers

from .models import Category, Game


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title_category']


class GameSerializer(CategorySerializer):
    class Meta(CategorySerializer.Meta):
        model = Game
        fields = '__all__'


class GameSerializer2(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Game
        fields = ('name', 'publisher', 'price', 'image', 'file', 'category',)
        read_only_fields = ['image', 'file']


class GameImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['image']


class GameFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['file']

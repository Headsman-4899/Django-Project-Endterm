from django.shortcuts import render
from .models import Category, Game
from .serializers import GameSerializer, CategorySerializer, GameSerializer2, GameImageSerializer
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework import viewsets, parsers
from rest_framework.response import Response
from rest_framework import decorators

import logging

logr = logging.getLogger(__name__)


# Create your views here.
@api_view(['GET'])
def CategoryList(request):
    logr.error('CategoryList def worked!')
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def category_detailed(request, pk):
    logr.error('Category_detailed def worked!')
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


class GamesViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Game.objects.all()
        serializer = GameSerializer(queryset, many=True)
        return Response(serializer.data)


class GamesNestedViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer2


class CreateGameSerializer(viewsets.ModelViewSet):
    serializer_class = GameSerializer


class CreateViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    parser_classes = [parsers.MultiPartParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

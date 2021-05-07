from django.shortcuts import render
from .models import Review
from .serializers import ReviewSerializer, ReviewModelSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.
import logging

logr = logging.getLogger(__name__)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def list(self, request, *args, **kwargs):
        logr.error('Review List worked!')
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        logr.error('Review Retrieve worked!')
        instance = self.get_object()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ReviewCreate(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer

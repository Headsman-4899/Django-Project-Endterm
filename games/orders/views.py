from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Order
from .serializers import (
    OrderSerializer,
)

import logging

logr = logging.getLogger(__name__)


# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        logr.error('Order List worked!')
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

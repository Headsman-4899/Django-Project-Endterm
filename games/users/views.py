from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from .models import Publisher, Customer
from rest_framework.response import Response
from users.serializers import PublisherSerializer, CustomerSerializer
from django.db.models import signals

import logging

logr = logging.getLogger(__name__)


# Create your views here.

class PublisherListCreateView(generics.ListCreateAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
    filter_fields = ['firstname']

    def get(self, request, *args, **kwargs):
        logr.error('Publisher worked!')
        return super().get(request, *args, **kwargs)


class PublisherDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


class CustomerListCreateView(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filter_fields = ['firstname']

    def get(self, request, *args, **kwargs):
        logr.error('Customer worked!')
        return super().get(request, *args, **kwargs)


class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class CustomerViewSet(viewsets.ViewSet):
    def list(self, request):
        logr.warning('Customer Listed')
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Customer.objects.all()
        customer = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)


class PublisherViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Publisher.objects.all()
        serializer = PublisherSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Publisher.objects.all()
        publisher = get_object_or_404(queryset, pk=pk)
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)

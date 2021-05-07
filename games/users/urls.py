from django.urls import path
from users.views import (
    PublisherListCreateView, PublisherDetailView,
    CustomerListCreateView, CustomerDetailView,
    CustomerViewSet, PublisherViewSet
)
app_name = 'users'

urlpatterns = [
    path('publisher', PublisherListCreateView.as_view(), name='list_create_publisher'),
    path('publisher/<int:pk>', PublisherDetailView.as_view(), name='rud_publisher'),
    path('customer', CustomerListCreateView.as_view(), name='list_create_customer'),
    path('customer/<int:pk>', CustomerDetailView.as_view(), name='rud_customer'),
    path('customerView/', CustomerViewSet.as_view({'get':'list'})),
    path('customerView/<int:pk>/', CustomerViewSet.as_view({'get': 'retrieve'})),
    path('publisherView/', PublisherViewSet.as_view({'get':'list'})),
    path('publisherView/<int:pk>/', PublisherViewSet.as_view({'get': 'retrieve'})),

]
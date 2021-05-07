from django.urls import path
from orders.views import (
    OrderViewSet,
)

app_name = 'orders'

urlpatterns = [
    #path('categories/<int:id>/', views.category_detailed),
    path('orders/', OrderViewSet.as_view({'get': 'list'})),
]
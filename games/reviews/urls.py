from django.urls import path
from reviews.views import (
    ReviewViewSet, ReviewCreate
)
app_name = 'users'

urlpatterns = [
    path('reviewlist', ReviewViewSet.as_view({'get':'list'})),
    path('reviewretrieve/<int:pk>', ReviewViewSet.as_view({'get':'retrieve'})),
    path('reviewcreate', ReviewCreate.as_view({'post':'create'})),
]
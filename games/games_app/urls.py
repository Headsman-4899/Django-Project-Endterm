from django.urls import path
from games_app import views
from games_app.views import (
    GamesViewSet, GamesNestedViewSet, CreateViewSet,
    CreateGameSerializer,
)

app_name = 'games_app'

urlpatterns = [
    # path('categories/<int:id>/', views.category_detailed),
    path('categories/', views.CategoryList),
    path('categories/<str:pk>/', views.category_detailed),
    path('games/', GamesViewSet.as_view({'get': 'list'})),
    path('games2/', GamesNestedViewSet.as_view({'get': 'list'})),
    path('gamescreate/', CreateViewSet.as_view({'post': 'create'})),
    # path('gamescreateimag', CreateViewSet.as_view({'put': 'image'}))
]

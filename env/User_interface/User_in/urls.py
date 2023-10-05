from django.urls import path
from rest_framework.schemas import get_schema_view

from . import views

urlpatterns = [
    path('register/', views.CustomUserCreateView.as_view(), name='register'),
    path('login/', views.CustomUserLoginView.as_view(), name='login'),
    path('profile/', views.UserProfileDetailView.as_view(), name='profile'),
    path('other-data/', views.OtherUserDataDetailView.as_view(), name='other-data'),
    path('delete-account/', views.CustomUserDeleteView.as_view(), name='delete-account'),
    # Добавьте другие маршруты по мере необходимости
]

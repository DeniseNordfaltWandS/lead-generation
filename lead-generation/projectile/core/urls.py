from django.urls import path
from .views import UserCreateView

# paths
app_name = 'core'

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create-view'),
]
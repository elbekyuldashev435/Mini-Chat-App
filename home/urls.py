from django.urls import path
from .views import UserListView


app_name = 'home'
urlpatterns = [
    path('', UserListView.as_view(), name='users-list'),
]
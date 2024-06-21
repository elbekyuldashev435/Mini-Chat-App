from django.urls import path

from .views import MyProfileView, ProfileView, Registration, Login, Logout, get_choice, EditProfile


app_name = 'users'
urlpatterns = [
    path('', get_choice, name='users'),
    path('profile/', MyProfileView.as_view(), name='my-profile'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('edit-profile/<int:pk>/', EditProfile.as_view(), name='edit-profile'),

    path('register/', Registration.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
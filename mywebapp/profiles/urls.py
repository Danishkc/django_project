from django.urls import path
from .views import login_view, profile_update, register
from .api_views import api_login, api_register, api_profile_update

urlpatterns = [
    path('', login_view, name='login'),
    path('profile/update/', profile_update, name='profile_update'),
    path('register/', register, name='register'),

    # API endpoints
    path('api/login/', api_login, name='api_login'),
    path('api/register/', api_register, name='api_register'),
    path('api/profile/update/', api_profile_update, name='api_profile_update'),
]
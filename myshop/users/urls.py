from django.urls import path
from .views import register, custom_logout, profile, seller_profile
from django.contrib.auth.views import LoginView

app_name = 'users'

urlpatterns = [
    path("register/", register, name='register'),
    path("login/", LoginView.as_view(template_name='login.html'), name="login"),
    path("logout/", custom_logout, name="logout"),
    path("profile/", profile, name='profile'),
    path("sellerprofile/<int:id>", seller_profile, name='sellerprofile')
]

from django.urls import path
from .views import RegisterView, LogoutAPIView, VerifyEmail, LoginAPIView, VerifyEmailAgainView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('email-verify/', VerifyEmail.as_view(), name="email-verify"),
    path('email-verify-again', VerifyEmailAgainView.as_view(), name="email-verify-again")

]

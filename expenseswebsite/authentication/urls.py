from .views import *
from django.urls import path

urlpatterns = [
    path("register", RegistrationView.as_view(), name="register")
]

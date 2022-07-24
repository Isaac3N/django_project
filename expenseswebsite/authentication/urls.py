from .views import *
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

urlpatterns = [
    path("register", RegistrationView.as_view(), name="register"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
    path("validate-username", csrf_exempt(UsernameValidationView.as_view()),
         name="validate-username"),
    path("validate-email", csrf_exempt(EmailValidationView.as_view()),
         name="validate-email"),
    path("activate/<uidb64>/<token>", VerificationView.as_view(), name="activate"),
    path("set-new-password/<uidb64>/<token>",
         CompletePasswordReset.as_view(), name="reset-user-password"),
    path("request-reset-link", RequestPasswordResetEmail.as_view(),
         name="request-password")

]

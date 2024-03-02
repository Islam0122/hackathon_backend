from django.urls import path
from .views import RegistrationView, ActivationView, LoginView, LogoutView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('activate/', ActivationView.as_view(), name='activate'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

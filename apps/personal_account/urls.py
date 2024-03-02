from django.urls import path
from .views import DoctorProfileView

urlpatterns = [
    path('profile/', DoctorProfileView.as_view(), name='doctor_profile'),

]
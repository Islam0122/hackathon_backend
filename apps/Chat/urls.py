from django.urls import path
from apps.Chat.Patient.views import *
from apps.Chat.gpt.views import *

urlpatterns = [
    path('', PatientViewSet.as_view({
        'get': 'list', 'post': 'create'
    }), name='patient-list'),
    path('<int:pk>/', PatientViewSet.as_view({
        'get': 'retrieve',
    }), name='patient-detail'),
    path('<int:pk>/chat/', GPTResponseApiView.as_view()),

]
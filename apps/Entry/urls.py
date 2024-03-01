from django.urls import path
from .views import EntryViewSet

urlpatterns = [
    path('',EntryViewSet.as_view({
        'get': 'list',
    }), name='patient-list'),
    path('<int:pk>/', EntryViewSet.as_view({
        'get': 'retrieve',
    }), name='patient-detail'),
]
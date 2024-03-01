from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CategoryViewSet, EntryViewSet

category_list = CategoryViewSet.as_view({'get': 'list',})
category_detail = CategoryViewSet.as_view({'get': 'retrieve',})

entry_list = EntryViewSet.as_view({'get': 'list',})
entry_detail = EntryViewSet.as_view({'get': 'retrieve',})

urlpatterns = [
    path('categories/', category_list, name='category-list'),
    path('categories/<int:pk>/', category_detail, name='category-detail'),
    path('categories/<int:pk>/entries/', CategoryViewSet.as_view({'get': 'entries'}), name='category-entries'),
    path('', entry_list, name='entry-list'),
    path('<int:pk>/', entry_detail, name='entry-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
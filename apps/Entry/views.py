from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Category, Entry
from .serializers import CategorySerializer, EntrySerializer
from django.shortcuts import get_object_or_404
from rest_framework import status


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def entries(self, request, pk=None):
        category = get_object_or_404(Category, pk=pk)
        entries = Entry.objects.filter(category=category)
        serializer = EntrySerializer(entries, many=True)
        return Response(serializer.data)


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

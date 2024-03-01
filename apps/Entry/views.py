from rest_framework import viewsets
from .models import Entry
from .serializers import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    lookup_field = 'pk'




from rest_framework import viewsets
from .serializers import ToDoSerializer
from .models import ToDo

class ToDoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ToDo.objects.all().order_by('-created_at')
    serializer_class = ToDoSerializer
    permission_classes = []

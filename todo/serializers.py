from rest_framework import serializers
from .models import ToDo


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'created_at']
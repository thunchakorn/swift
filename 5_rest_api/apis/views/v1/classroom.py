from django.db.models import Count

from rest_framework import viewsets

from apis.models import Classroom
from apis.serializers import (
    ClassroomListSerializer,
    ClassroomSerializer,
    ClassroomCreateSerializer,
)
from apis.filters import ClassroomFilter


class ClassroomViewSet(viewsets.ModelViewSet):
    model = Classroom

    def get_queryset(self):
        qs = Classroom.objects.all()

        self.filterset = ClassroomFilter(self.request.GET, queryset=qs)

        return self.filterset.qs

    def get_serializer_class(self):
        if self.action == "list":
            return ClassroomListSerializer

        if self.action in ["create", "update", "partial_update"]:
            return ClassroomCreateSerializer

        return ClassroomSerializer

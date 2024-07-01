from rest_framework import viewsets

from apis.models import Teacher
from apis.serializers import (
    TeacherListSerializer,
    TeacherSerializer,
    TeacherCreateSerializer,
)
from apis.filters import TeacherFilter


class TeacherViewSet(viewsets.ModelViewSet):
    model = Teacher

    def get_queryset(self):
        qs = Teacher.objects.all()

        self.filterset = TeacherFilter(self.request.GET, queryset=qs)

        return self.filterset.qs

    def get_serializer_class(self):
        if self.action == "list":
            return TeacherListSerializer

        if self.action in ["create", "update", "partial_update"]:
            return TeacherCreateSerializer

        return TeacherSerializer

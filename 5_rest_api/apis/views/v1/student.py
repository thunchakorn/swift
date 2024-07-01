from rest_framework import viewsets

from apis.models import Student
from apis.serializers import (
    StudentListSerializer,
    StudentSerializer,
    StudentCreatetSerializer,
)
from apis.filters import StudentFilter


class StudentViewSet(viewsets.ModelViewSet):
    model = Student

    def get_queryset(self):
        qs = Student.objects.all()

        self.filterset = StudentFilter(self.request.GET, queryset=qs)

        return self.filterset.qs

    def get_serializer_class(self):
        if self.action == "list":
            return StudentListSerializer

        if self.action in ["create", "update", "partial_update"]:
            return StudentCreatetSerializer

        return StudentSerializer

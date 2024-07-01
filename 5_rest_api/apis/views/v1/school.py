from django.db.models import Count

from rest_framework import viewsets

from apis.models import School
from apis.serializers import SchoolListSerializer, SchoolSerializer
from apis.filters import SchoolFilter


class SchoolViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        qs = School.objects.annotate(
            count_classroom=Count("classrooms", distinct=True),
            count_teacher=Count("classrooms__teachers", distinct=True),
            count_student=Count("classrooms__students", distinct=True),
        )

        self.filterset = SchoolFilter(self.request.GET, queryset=qs)

        return self.filterset.qs

    def get_serializer_class(self):
        if self.action == "list":
            return SchoolListSerializer
        return SchoolSerializer

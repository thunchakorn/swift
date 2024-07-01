import django_filters

from .models import School, Classroom, Teacher, Student


class SchoolFilter(django_filters.FilterSet):
    class Meta:
        model = School
        fields = ["name"]

    name = django_filters.CharFilter("name", lookup_expr="icontains")


class ClassroomFilter(django_filters.FilterSet):
    class Meta:
        model = Classroom
        fields = ["school"]

    school = django_filters.CharFilter("school", lookup_expr="iexact")


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = ["firstname", "lastname", "gender", "school"]

    firstname = django_filters.CharFilter("firstname", lookup_expr="icontains")
    lastname = django_filters.CharFilter("lastname", lookup_expr="icontains")
    gender = django_filters.CharFilter("gender", lookup_expr="iexact")
    school = django_filters.CharFilter("classrooms__school", lookup_expr="exact")
    classrooms = django_filters.CharFilter("classrooms", lookup_expr="exact")


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ["firstname", "lastname", "gender", "school"]

    firstname = django_filters.CharFilter("firstname", lookup_expr="icontains")
    lastname = django_filters.CharFilter("lastname", lookup_expr="icontains")
    gender = django_filters.CharFilter("gender", lookup_expr="iexact")
    school = django_filters.CharFilter("classroom__school", lookup_expr="exact")
    classroom = django_filters.CharFilter("classroom", lookup_expr="exact")

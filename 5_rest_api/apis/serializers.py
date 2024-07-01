from rest_framework import serializers

from .models import School, Classroom, Teacher, Student, Gender


# School
# ----------------------------------------------------------------------
class SchoolListSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ["url", "abbreviation"]

    url = serializers.HyperlinkedIdentityField(view_name="v1:school-detail")


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = [
            "id",
            "name",
            "abbreviation",
            "address",
            "count_classroom",
            "count_teacher",
            "count_student",
        ]

    count_classroom = serializers.IntegerField(read_only=True)
    count_teacher = serializers.IntegerField(read_only=True)
    count_student = serializers.IntegerField(read_only=True)


# Classroom
# ----------------------------------------------------------------------
class ClassroomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ["url", "year", "room", "school"]

    url = serializers.HyperlinkedIdentityField(view_name="v1:classroom-detail")


class ClassroomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ["year", "room", "school"]


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ["id", "year", "room", "school", "teachers", "students"]

    school = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="v1:school-detail"
    )

    teachers = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="v1:teacher-detail"
    )
    students = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="v1:student-detail"
    )


# Teacher
# ----------------------------------------------------------------------
class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["url", "firstname", "lastname", "gender"]

    url = serializers.HyperlinkedIdentityField(view_name="v1:teacher-detail")


class TeacherCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "firstname", "lastname", "gender", "classrooms"]

    gender = serializers.ChoiceField(choices=Gender)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id", "firstname", "lastname", "gender", "classrooms"]

    gender = serializers.ChoiceField(choices=Gender)
    classrooms = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="v1:classroom-detail"
    )


# Student
# ----------------------------------------------------------------------
class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["url", "firstname", "lastname", "gender", "classroom"]

    url = serializers.HyperlinkedIdentityField(view_name="v1:student-detail")


class StudentCreatetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["firstname", "lastname", "gender", "classroom"]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "firstname", "lastname", "gender", "classroom"]

    gender = serializers.ChoiceField(choices=Gender)
    classroom = serializers.HyperlinkedRelatedField(
        read_only=True, view_name="v1:classroom-detail"
    )

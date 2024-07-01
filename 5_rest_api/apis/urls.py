from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apis.views.v1 import school, classroom, teacher, student


router = DefaultRouter()

router.register(r"school", school.SchoolViewSet, basename="school")
router.register(r"classroom", classroom.ClassroomViewSet, basename="classroom")
router.register(r"teacher", teacher.TeacherViewSet, basename="teacher")
router.register(r"student", student.StudentViewSet, basename="student")

api_v1_urls = (router.urls, "v1")

urlpatterns = [path("v1/", include(api_v1_urls))]

from django.contrib import admin

from . import models

admin.site.register(models.School)
admin.site.register(models.Classroom)
admin.site.register(models.Teacher)
admin.site.register(models.Student)

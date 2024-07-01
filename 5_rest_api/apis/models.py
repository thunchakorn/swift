from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    address = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.name


class Classroom(models.Model):
    year = models.IntegerField()
    room = models.IntegerField()
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="classrooms"
    )

    def __str__(self) -> str:
        return f"{self.year}/{self.room}"


class Gender(models.TextChoices):
    m = "male"
    f = "female"


class Teacher(models.Model):

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=Gender)
    classrooms = models.ManyToManyField(to=Classroom, related_name="teachers")

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=Gender)
    classroom = models.ForeignKey(
        to=Classroom, on_delete=models.CASCADE, related_name="students"
    )

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"

from django.db import models


# Create your models here.
class Professor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Semester(models.Model):
    bezeichnung = models.CharField(max_length=100)

    def __str__(self):
        return self.bezeichnung


class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Kurs(models.Model):
    title = models.CharField(max_length=100)
    prof = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="kurse")
    semester = models.ForeignKey(
        Semester, on_delete=models.CASCADE, related_name="kurse"
    )
    students = models.ManyToManyField(Student, related_name="kurse")

    def __str__(self):
        return self.title


class Kursbeschreibung(models.Model):
    description = models.TextField()
    kurs = models.OneToOneField(Kurs, on_delete=models.CASCADE)

    def __str__(self):
        return self.kurs.title


class Studentenausweis(models.Model):
    number = models.CharField(max_length=10)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

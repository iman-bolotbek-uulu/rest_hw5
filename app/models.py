from django.db import models


class Student(models.Model):
    fullname = models.CharField(max_length=30)
    date_birth = models.DateField()

    def __str__(self):
        return self.fullname


class Mentor(models.Model):
    fullname = models.CharField(max_length=30)
    experience = models.IntegerField()

    def __str__(self):
        return self.fullname


class Course(models.Model):
    name = models.CharField(max_length=30)
    month = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



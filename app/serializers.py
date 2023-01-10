from rest_framework import serializers
from . import models


class CourseSerialize(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = "__all__"


class MentorSerialize(serializers.ModelSerializer):
    class Meta:
        model = models.Mentor
        fields = "__all__"


class StudentSerialize(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = "__all__"


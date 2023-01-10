from rest_framework import viewsets, generics, views
from . import models
from . import serializers
from . import my_generics


class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerialize


class StudentCreateListView(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerialize


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerialize


class MentorCreateAPIView(my_generics.MentorCreateAPIView):
    serializer_class = serializers.MentorSerialize
    model = models.Mentor

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MentorRetrieveUpdateDestroyAPIView(my_generics.RetrieveMixinAPI, my_generics.UpdateMixinAPI, my_generics.DeleteMixinAPI, my_generics.MentorAPIView):
    serializer_class = serializers.MentorSerialize
    model = models.Mentor

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
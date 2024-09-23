from rest_framework import serializers
from .models import CourseForm

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseForm
        fields = '__all__'

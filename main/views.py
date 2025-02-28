from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CourseForm
from .serializers import CourseSerializer
from django.shortcuts import render,redirect

class CourseFormListCreateView(APIView):
    def get(self, request):
        courses = CourseForm.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def index(request):
    forma = CourseForm.objects.all()

    ctx = {
        'forma':forma
    }
    return render(request,'index.html',ctx)
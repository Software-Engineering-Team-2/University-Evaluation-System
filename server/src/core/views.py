from django.shortcuts import render
from django.http import JsonResponse # Abbas: Is this being used?

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer, CourseSerializer, InstructorReviewSerializer
from .models import Post, Courses, Instructor_Review

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class getCourses(APIView):
    def get(self, request, *args, **kwargs):
        title = request.GET['title']
        if(title != ''):
            qs = Courses.objects.all().filter(title__contains=title)
        else:
            qs = Courses.objects.all()
        serializer = CourseSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class getInstructorReviews(APIView):
    # def get(self, request, *args, **kwargs):
    #     title = request.GET['title']
    #     if(title != ''):
    #         qs = Courses.objects.all().filter(title__contains=title)
    #     else:
    #         qs = Courses.objects.all()
    #     serializer = CourseSerializer(qs, many=True)
    #     return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = InstructorReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
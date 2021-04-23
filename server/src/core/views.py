from django.shortcuts import render
from django.http import JsonResponse # Abbas: Is this being used?

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CourseSerializer, InstructorReviewSerializer,InstructorSerializer, CourseReviewSerializer, CourseReviewTagSerializer
from .models import Course, Instructor_Review, Course_Review, Instructor, Course_Review_Tag


class getCourses(APIView):
    def get(self, request, *args, **kwargs):
        if ('title' in request.GET):
            query = request.GET['title']
            qs = Course.objects.all().filter(title__contains=query)
        elif ('id' in request.GET):
            query = request.GET['id']
            qs = Course.objects.all().filter(id=query)
        else:
            qs = Course.objects.all()
        serializer = CourseSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class getInstructor(APIView):
    def get(self, request, *args, **kwargs):
        if ('name' in request.GET):
            query = request.GET['name']
            qs = Instructor.objects.all().filter(name__contains=query)
        elif ('id' in request.GET):
            query = request.GET['id']
            qs = Instructor.objects.all().filter(id=query)
        else:
            qs = Instructor.objects.all()
        serializer = InstructorSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = InstructorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class getInstructorReviews(APIView):

    def get(self, request, *args, **kwargs):
        instructorID = request.GET['instructorID']
        qs = Instructor_Review.objects.all().filter(instructorID__exact=instructorID)
        serializer = InstructorReviewSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = InstructorReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class getCourseReviews(APIView):
    
    def get(self, request, *args, **kwargs):
        CourseID = request.GET['courseSemesterID']
        qs = Course_Review.objects.all().filter(courseSemesterID__exact=CourseID)
        serializer = CourseReviewSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CourseReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def patch(self, request, *args, **kwargs):
        print(request.data)
        reviewId = request.data['id']
        qs = Course_Review.objects.all().filter(id=reviewId).first()
        serializer = CourseReviewSerializer(qs, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class getInstructorReviews(APIView):

    def get(self, request, *args, **kwargs):
        print("request.data:",request.data)
        if('instructorID' in request.GET):
            instructorID = request.GET['instructorID']
            qs = Instructor_Review.objects.all().filter(instructorID__exact=instructorID)
        else:
            qs = Instructor_Review.objects.all()
        serializer = InstructorReviewSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = InstructorReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class CourseReviewTagView(APIView):

    def get(self, request, *args, **kwargs):

        ID = request.GET['courseReviewID']
        qs = Course_Review_Tag.objects.all().filter(courseReviewID__exact= ID)
        serializer = CourseReviewTagSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("request.data:",request.data)
        serializer = CourseReviewTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

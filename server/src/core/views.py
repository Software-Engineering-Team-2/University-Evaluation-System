from django.shortcuts import render
from django.http import JsonResponse # Abbas: Is this being used?

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *

from django_und.models import Vote


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
    
    def create_vote(self, course, user, vtype, val):
        vote = Vote(courseReviewID=course, userID=user, voteType=vtype)
        if vtype == "U":
            course.votes += val
        else:
            course.votes -= val
        vote.save()
        course.save()        

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
        id = request.data['id']
        courseReview = Course_Review.objects.get(id=id)
        if (request.data['type'] == "up"):
            courseReview.upvote(request.user)
        else:
            courseReview.downvote(request.user)
        serializer = CourseReviewSerializer(courseReview)
        return Response(serializer.data)

    
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

class InstructorReviewTagView(APIView):

    def get(self, request, *args, **kwargs):

        ID = request.GET['instructorReviewID']
        qs = Instructor_Review_Tag.objects.all().filter(instructorReviewID__exact= ID)
        serializer = InstructorReviewTagSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print("request.data:",request.data)
        serializer = InstructorReviewTagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class getCourseReviewVotes(APIView):

    def post(self, request, *args, **kwargs):
        try:
            vote = Vote.objects.get(user=request.user, object_id=request.data['courseReviewId'])
            return Response(VoteSerializer(vote).data)
        except Vote.DoesNotExist:
            return Response({}, status=400)

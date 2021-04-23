from rest_framework import serializers
from .models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id', 'title', 'description', 'school'
        )

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = (
            'id','name', 'email', 'description')

class InstructorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor_Review
        fields = (
            'instructorID', 'rating', 'comments','verified','anonymous','timeStamp'
        )

class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_Review
        fields = (
            'id', 'courseSemesterID', 'rating', 'comments','verified','anonymous','timeStamp', 'votes'
        )

# class CourseTagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = (
#             'courseReviewID', 'tagName'
#         )

class CourseReviewTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_Review_Tag
        fields = (
            'courseReviewID', 'tagID'
        )
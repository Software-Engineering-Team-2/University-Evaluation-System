from rest_framework import serializers
from .models import *
from django_und.models import Vote

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
            'id', 'instructorID', 'rating', 'comments','verified','anonymous','timeStamp', 'und_score'
        )

class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_Review
        fields = (
            'id', 'courseSemesterID', 'rating', 'comments','verified','anonymous','timeStamp', 'und_score'
        )

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = (
            'user', 'score', 'object_id'
        )
        
class InstructorReviewTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor_Review_Tag
        fields = (
            'instructorReviewID', 'tagID'
        )

class CourseReviewTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_Review_Tag
        fields = (
            'courseReviewID', 'tagID'
        )

class CourseTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_Tag
        fields = (
            'name'
        )

class instructorTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor_Tag
        fields = '__all__' 
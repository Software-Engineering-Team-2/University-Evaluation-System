from rest_framework import serializers
from .models import Course, Instructor_Review, Instructor,Course_Review

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
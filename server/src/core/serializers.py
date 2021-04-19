from rest_framework import serializers
from .models import Post, Courses, Instructor_Review

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 'description', 'owner'
        )

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = (
            'id', 'title', 'description', 'school'
        )

class InstructorReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor_Review
        fields = (
            'instructorID', 'rating', 'comments','verified','anonymous','timeStamp'
        )
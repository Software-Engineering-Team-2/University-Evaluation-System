from rest_framework import serializers
from .models import Post, Courses

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

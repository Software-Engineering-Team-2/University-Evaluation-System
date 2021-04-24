from django.contrib import admin

from .models import Courses, Instructor_Review, Instructor, Student,Semester, Course_Semester, Course_Review, Vote

admin.site.register(Courses)
admin.site.register(Instructor)
admin.site.register(Instructor_Review)
admin.site.register(Student)
admin.site.register(Semester)
admin.site.register(Course_Semester)
admin.site.register(Course_Review)
admin.site.register(Vote)

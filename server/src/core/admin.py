from django.contrib import admin

from .models import *

admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Instructor_Review)
admin.site.register(Student)
admin.site.register(Semester)
admin.site.register(Course_Semester)
admin.site.register(Course_Review)
admin.site.register(Tag)
admin.site.register(Course_Review_Tag)
admin.site.register(Instructor_Review_Tag)

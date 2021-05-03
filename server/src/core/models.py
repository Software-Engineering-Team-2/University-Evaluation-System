from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django_und.models import VoteMixin

User = get_user_model()
SCHOOL_TYPES = [('DSSE', 'Dhanani School of Science & Engineering'), ('AHSS', 'School of Arts, Humanities & Social Sciences')]

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)
    school = models.CharField(max_length=100, choices=SCHOOL_TYPES)

    def __str__(self):
        return self.title


class Instructor(models.Model):
    #instructorID = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    #studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    #courseID = models.ForeignKey(Course, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    description = models.TextField() # Will this be CharField or TextField is fine?
    
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contactNumber = models.CharField(max_length=50)
    Batch = models.PositiveSmallIntegerField()
    Major = models.CharField(max_length=100)
    Minor = models.CharField(max_length=100)

class Instructor_Review(VoteMixin, models.Model):
    # null is set to trutemporarily
    instructorID = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True)
    # studentID = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    #courseID = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    rating = models.FloatField(validators = [MaxValueValidator(5)])
    comments = models.TextField() # Will Specify max_length maybe later..
    verified = models.BooleanField(default = False)
    anonymous = models.BooleanField(default = True)
    timeStamp = models.DateTimeField(auto_now_add=True)


class Semester(models.Model):
    year = models.PositiveSmallIntegerField()
    season = models.CharField(max_length=50) # Might add validators later

class Course_Semester(models.Model):
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)
    semesterID = models.ForeignKey(Semester, on_delete=models.CASCADE)

class Course_Review(VoteMixin, models.Model):
    courseSemesterID = models.ForeignKey(Course, on_delete=models.CASCADE)
    # studentID = models.ForeignKey(Student, on_delete=models.CASCADE)

    rating = models.FloatField(validators = [MaxValueValidator(5)])
    comments = models.TextField() # Will Specify max_length maybe later..
    verified = models.BooleanField(default = False)
    anonymous = models.BooleanField(default = True)
    timeStamp = models.DateTimeField(auto_now_add=True)

class Course_Tag(models.Model):
    name = models.CharField(max_length=100)

class Course_Review_Tag(models.Model):
    courseReviewID = models.ForeignKey(Course_Review, on_delete=models.CASCADE)
    tagID = models.ForeignKey(Course_Tag, on_delete=models.CASCADE)

class Instructor_Tag(models.Model):
    name = models.CharField(max_length=100)

class Instructor_Review_Tag(models.Model):
    instructorReviewID = models.ForeignKey(Instructor_Review, on_delete=models.CASCADE)
    tagID = models.ForeignKey(Instructor_Tag, on_delete=models.CASCADE)



    


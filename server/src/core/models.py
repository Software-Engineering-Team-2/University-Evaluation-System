from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
SCHOOL_TYPES = [('DSSE', 'Dhanani School of Science & Engineering'), ('AHSS', 'School of Arts, Humanities & Social Sciences')]

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Courses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)
    school = models.CharField(max_length=100, choices=SCHOOL_TYPES)

    def __str__(self):
        return self.title

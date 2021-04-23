# Generated by Django 3.1.7 on 2021-04-21 20:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_course_review_course_semester_instructor_instructor_review_post_semester_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_review',
            name='rating',
            field=models.FloatField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]

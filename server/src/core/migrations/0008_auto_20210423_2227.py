# Generated by Django 3.1.7 on 2021-04-23 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210423_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_review',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]

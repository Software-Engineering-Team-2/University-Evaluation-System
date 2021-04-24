# Generated by Django 3.1.7 on 2021-04-23 17:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210423_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='object_id',
        ),
        migrations.AddField(
            model_name='activity',
            name='voted_object_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]

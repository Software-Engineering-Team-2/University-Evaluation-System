# Generated by Django 3.1.7 on 2021-04-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210410_0152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('school', models.CharField(choices=[('DSSE', 'Dhanani School of Science & Engineering'), ('AHSS', 'School of Arts, Humanities & Social Sciences')], max_length=100)),
            ],
        ),
    ]

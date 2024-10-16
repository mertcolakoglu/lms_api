# Generated by Django 5.1.2 on 2024-10-13 19:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        ('metarials', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_accessed', models.DateTimeField(auto_now=True)),
                ('completion_percentage', models.FloatField(default=0.0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_progress', to='courses.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
        migrations.CreateModel(
            name='LectureProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('last_accessed', models.DateTimeField(auto_now=True)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metarials.lecture')),
                ('progress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecture_progress', to='progress.progress')),
            ],
            options={
                'unique_together': {('progress', 'lecture')},
            },
        ),
        migrations.CreateModel(
            name='AssignmentProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_submitted', models.BooleanField(default=False)),
                ('score', models.FloatField(blank=True, null=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metarials.assignment')),
                ('progress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_progress', to='progress.progress')),
            ],
            options={
                'unique_together': {('progress', 'assignment')},
            },
        ),
    ]

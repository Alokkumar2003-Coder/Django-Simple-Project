# Generated by Django 5.1.4 on 2025-01-07 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0004_department_studentid_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_age',
            field=models.IntegerField(default=18),
        ),
    ]

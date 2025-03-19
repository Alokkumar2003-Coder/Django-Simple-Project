# Generated by Django 5.1.4 on 2025-01-05 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=500)),
                ('speed', models.IntegerField(default=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-04 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=100)),
                ('course_dec', models.TextField(max_length=200)),
                ('course_duration', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshop_title', models.CharField(max_length=100)),
                ('workshop_dec', models.TextField(max_length=200)),
                ('workshop_duration', models.CharField(max_length=20)),
            ],
        ),
    ]
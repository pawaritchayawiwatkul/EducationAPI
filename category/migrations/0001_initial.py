# Generated by Django 4.2.13 on 2024-08-21 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListeningPracticeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=10)),
                ('image_url', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SpeakingPracticeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=10)),
                ('image_url', models.FileField(upload_to='')),
            ],
        ),
    ]
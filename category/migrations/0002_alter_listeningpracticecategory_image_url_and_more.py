# Generated by Django 4.2.13 on 2024-08-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listeningpracticecategory',
            name='image_url',
            field=models.FileField(upload_to='images/category'),
        ),
        migrations.AlterField(
            model_name='speakingpracticecategory',
            name='image_url',
            field=models.FileField(upload_to='images/category'),
        ),
    ]

# Generated by Django 4.2.13 on 2024-08-21 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0005_remove_listeningpractice_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speakingtargets',
            name='text',
            field=models.TextField(max_length=2000),
        ),
    ]

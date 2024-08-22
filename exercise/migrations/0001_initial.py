# Generated by Django 4.2.13 on 2024-08-21 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListeningPractice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=10)),
                ('image_url', models.FileField(upload_to='')),
                ('released_date', models.DateField(auto_now_add=True)),
                ('number_of_plays', models.IntegerField()),
                ('question_amount', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='practices', to='category.listeningpracticecategory')),
            ],
        ),
        migrations.CreateModel(
            name='SpeakingPractice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('practice_type', models.CharField(choices=[('SW', 'Speaking Word Practice'), ('SS', 'Speaking Sentence Practice'), ('SP', 'Speaking Paragraph Practice')], default='SW', max_length=2)),
                ('image_url', models.FileField(upload_to='')),
                ('released_date', models.DateField(auto_now_add=True)),
                ('number_of_plays', models.IntegerField()),
                ('question_amount', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.listeningpracticecategory')),
            ],
        ),
        migrations.CreateModel(
            name='SpeakingTargets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('targets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='targets', to='exercise.speakingpractice')),
            ],
        ),
        migrations.CreateModel(
            name='ListeningQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField()),
                ('choice1', models.CharField(max_length=255)),
                ('choice2', models.CharField(max_length=255)),
                ('choice3', models.CharField(max_length=255)),
                ('choice4', models.CharField(max_length=255)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='exercise.listeningpractice')),
            ],
        ),
    ]
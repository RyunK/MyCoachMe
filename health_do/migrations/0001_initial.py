# Generated by Django 3.2.19 on 2023-05-19 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0002_alter_user_data_lack_health'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train_video',
            fields=[
                ('video_name', models.CharField(max_length=20)),
                ('video_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('main_body', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Training_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rarm', models.FloatField()),
                ('Larm', models.FloatField()),
                ('Relbow', models.FloatField()),
                ('Lelbow', models.FloatField()),
                ('Rwaist', models.FloatField()),
                ('Lwaist', models.FloatField()),
                ('Rleg', models.FloatField()),
                ('Lleg', models.FloatField()),
                ('Rknee', models.FloatField()),
                ('Lknee', models.FloatField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user_data')),
                ('video_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health_do.train_video')),
            ],
        ),
    ]

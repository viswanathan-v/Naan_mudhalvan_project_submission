# Generated by Django 5.0.3 on 2024-04-05 04:35

import disco.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to=disco.models.getFileName)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-show|1-Hidden')),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('Singer', models.CharField(max_length=150)),
                ('writer', models.CharField(max_length=150)),
                ('song_image', models.ImageField(blank=True, null=True, upload_to=disco.models.getFileName)),
                ('audio_file', models.FileField(upload_to='audio/')),
                ('language', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False, help_text='0-show|1-Hidden')),
                ('Trending', models.BooleanField(default=False, help_text='0-normal|1-trend')),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disco.category')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-24 01:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'content_tag',
            },
        ),
        migrations.CreateModel(
            name='ContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'content_type',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('body', tinymce.models.HTMLField()),
                ('description', tinymce.models.HTMLField()),
                ('thumbnail_image', models.ImageField(blank=True, upload_to='content/thumbs/')),
                ('header_image', models.ImageField(blank=True, upload_to='content/headers/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField()),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ManyToManyField(to='content.ContentType')),
                ('tags', models.ManyToManyField(to='content.ContentTag')),
            ],
            options={
                'db_table': 'content_post',
            },
        ),
    ]
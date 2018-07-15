# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-15 13:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Arendator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(default='unknown', max_length=200)),
                ('email', models.CharField(default='unknown', max_length=200)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_time_day', models.IntegerField(default=0)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('rent_finish_date', models.DateTimeField(blank=True, null=True)),
                ('price_dollar', models.IntegerField(default=0)),
                ('payment_by_contract_dollar', models.IntegerField(default=0)),
                ('contract_file', models.FileField(blank=True, null=True, upload_to='contracts/')),
                ('rental_condition', models.CharField(choices=[(None, 'unknown'), ('free', 'free'), ('leased', 'leased')], default='free', max_length=6)),
                ('arendator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpapp.Arendator')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(default='unknown', max_length=200)),
                ('text', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('rental_condition', models.CharField(choices=[(None, 'unknown'), ('free', 'free'), ('leased', 'leased')], default='free', max_length=6)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='rent_obj',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpapp.Post'),
        ),
    ]

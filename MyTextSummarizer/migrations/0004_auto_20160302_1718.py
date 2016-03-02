# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyTextSummarizer', '0003_auto_20160301_0508'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=1000, upload_to='files/')),
            ],
        ),
        migrations.AlterField(
            model_name='sentance',
            name='order',
            field=models.IntegerField(),
        ),
    ]

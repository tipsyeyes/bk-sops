# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-01 09:09
from __future__ import absolute_import, unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterFailInstanceArchive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_type', models.CharField(max_length=128, verbose_name='\u8d44\u6e90\u7c7b\u578b')),
                ('instances', models.TextField(verbose_name='\u8d44\u6e90\u4fe1\u606f')),
                ('scope_id', models.CharField(max_length=128, verbose_name='\u4f5c\u7528\u57df ID')),
            ],
        ),
    ]

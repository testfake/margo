# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinksPostTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_name', models.CharField(max_length=200)),
                ('post_text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='linksposttag',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
        ),
        migrations.AddField(
            model_name='linksposttag',
            name='tag',
            field=models.ForeignKey(to='blog.Tag'),
        ),
    ]

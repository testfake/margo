# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('autor', models.CharField(verbose_name='Автор', max_length=200)),
                ('comment_name', models.CharField(verbose_name='Заголовок', max_length=200)),
                ('comment_text', models.TextField(verbose_name='Комментарий')),
                ('pub_date', models.DateTimeField(verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.RenameModel(
            old_name='LinksPostTag',
            new_name='PostsToTags',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
        migrations.AlterField(
            model_name='post',
            name='post_name',
            field=models.CharField(verbose_name='Название поста', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(verbose_name='Наименование', max_length=200),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]

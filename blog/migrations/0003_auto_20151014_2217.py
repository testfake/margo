# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151012_2001'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostsToTags',
            new_name='Tags',
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'Тэг', 'verbose_name_plural': 'Тэги'},
        ),
    ]

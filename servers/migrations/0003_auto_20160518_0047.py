# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0002_auto_20160518_0024'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Server',
        ),
        migrations.RemoveField(
            model_name='school',
            name='school_address',
        ),
        migrations.AddField(
            model_name='classroom',
            name='classroom_name',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='student',
            name='school',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_name',
            field=models.TextField(default=b''),
        ),
    ]

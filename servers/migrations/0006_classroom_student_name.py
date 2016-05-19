# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0005_auto_20160519_0443'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='student_name',
            field=models.TextField(default=b''),
        ),
    ]

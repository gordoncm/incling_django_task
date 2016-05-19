# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0003_auto_20160518_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='school',
        ),
        migrations.AddField(
            model_name='school',
            name='classroom',
            field=models.ForeignKey(default=b'', to='servers.Classroom'),
        ),
    ]

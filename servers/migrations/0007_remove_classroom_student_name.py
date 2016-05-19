# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0006_classroom_student_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='student_name',
        ),
    ]

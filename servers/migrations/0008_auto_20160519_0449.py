# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0007_remove_classroom_student_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='classroom_name',
            new_name='classroom',
        ),
        migrations.AddField(
            model_name='classroom',
            name='student',
            field=models.ForeignKey(default=b'', to='servers.Student'),
        ),
    ]

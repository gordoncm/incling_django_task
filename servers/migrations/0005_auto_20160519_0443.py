# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0004_auto_20160519_0443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='classroom',
            new_name='classroom_name',
        ),
    ]

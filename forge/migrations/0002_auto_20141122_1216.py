# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forge', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='supported',
            field=models.BooleanField(default=False, db_index=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='release',
            name='supported',
            field=models.BooleanField(default=False, db_index=True),
            preserve_default=True,
        ),
    ]

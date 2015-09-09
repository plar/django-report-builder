# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report_builder', '0005_auto_20150904_1943'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='displayfield',
            options={'ordering': ['position'], 'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
        migrations.AlterModelOptions(
            name='filterfield',
            options={'ordering': ['position'], 'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
        migrations.AlterModelOptions(
            name='format',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
    ]

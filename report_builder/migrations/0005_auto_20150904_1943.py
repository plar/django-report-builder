# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report_builder', '0004_report_general_report'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report_builder', '0003_auto_20150804_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='general_report',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

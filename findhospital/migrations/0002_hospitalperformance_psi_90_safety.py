# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findhospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitalperformance',
            name='PSI_90_SAFETY',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=3),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findhospital', '0003_remove_hospitalperformance_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitalperformance',
            name='Score',
            field=models.DecimalField(default=1, max_digits=10, decimal_places=3),
            preserve_default=False,
        ),
    ]

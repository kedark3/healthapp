# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findhospital', '0002_hospitalperformance_psi_90_safety'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospitalperformance',
            name='Score',
        ),
    ]

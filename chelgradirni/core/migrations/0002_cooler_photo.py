# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0008_auto_20150509_1557'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooler',
            name='photo',
            field=models.ForeignKey(verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0413\u0412\u041f', blank=True, to='photologue.Photo', null=True),
        ),
    ]

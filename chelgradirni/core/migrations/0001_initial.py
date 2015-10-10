# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cooler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True)),
                ('performance', models.CharField(max_length=5, verbose_name='\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c', blank=True)),
                ('load', models.CharField(max_length=5, verbose_name='\u0422\u0435\u043f\u043b\u043e\u0432\u0430\u044f \u043d\u0430\u0433\u0440\u0443\u0437\u043a\u0430', blank=True)),
                ('drop', models.CharField(max_length=5, verbose_name='\u041f\u0435\u0440\u0435\u043f\u0430\u0434 \u0442\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440', blank=True)),
                ('power', models.CharField(max_length=5, verbose_name='\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c \u0432\u0435\u043d\u0442\u0435\u043b\u044f\u0442\u043e\u0440\u0430', blank=True)),
                ('weight', models.CharField(max_length=5, verbose_name='\u041c\u0430\u0441\u0441\u0430', blank=True)),
                ('dimension', models.CharField(max_length=15, verbose_name='\u0413\u0430\u0431\u0430\u0440\u0438\u0442\u043d\u044b\u0435 \u0440\u0430\u0437\u043c\u0435\u0440\u044b', blank=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('siscontas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('last_four_digits', models.IntegerField()),
                ('card_type', models.TextField()),
                ('day_close_account', models.IntegerField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2015, 12, 9, 1, 28, 46, 484023, tzinfo=utc))),
                ('edited_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RenameModel(
            old_name='Banco',
            new_name='Bank',
        ),
        migrations.RenameField(
            model_name='bank',
            old_name='descricao',
            new_name='description',
        ),
        migrations.AddField(
            model_name='card',
            name='bank',
            field=models.ForeignKey(to='siscontas.Bank'),
        ),
    ]

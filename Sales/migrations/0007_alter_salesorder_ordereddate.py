# Generated by Django 4.1.4 on 2022-12-15 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0006_alter_salesorder_ordereddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='OrderedDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 15, 18, 21, 13, 395680, tzinfo=datetime.timezone.utc)),
        ),
    ]

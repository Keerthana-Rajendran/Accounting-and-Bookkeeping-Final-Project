# Generated by Django 4.1.3 on 2022-12-08 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Purchase', '0004_alter_orders_ordereddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='OrderedDate',
            field=models.DateField(default=datetime.datetime(2022, 12, 8, 17, 19, 22, 534859)),
        ),
        migrations.AlterField(
            model_name='vendororder',
            name='Ordereddate',
            field=models.DateField(default=datetime.datetime(2022, 12, 8, 17, 19, 22, 535903)),
        ),
    ]
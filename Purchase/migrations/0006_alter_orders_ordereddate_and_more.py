# Generated by Django 4.1.4 on 2022-12-15 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Purchase', '0005_alter_orders_ordereddate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='OrderedDate',
            field=models.DateField(default=datetime.datetime(2022, 12, 15, 6, 54, 22, 577002)),
        ),
        migrations.AlterField(
            model_name='vendororder',
            name='Ordereddate',
            field=models.DateField(default=datetime.datetime(2022, 12, 15, 6, 54, 22, 577002)),
        ),
    ]

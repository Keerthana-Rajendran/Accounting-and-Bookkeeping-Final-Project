# Generated by Django 4.1.4 on 2022-12-15 14:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banking', '0005_alter_credit_amount_date_alter_withdraw_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit_amount',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 12, 15, 6, 54, 22, 608307)),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 12, 15, 6, 54, 22, 608307)),
        ),
    ]
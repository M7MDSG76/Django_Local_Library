# Generated by Django 3.1.7 on 2022-06-06 20:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_auto_20220606_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarymember',
            name='membership_start_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 6, 20, 13, 59, 900451, tzinfo=utc), verbose_name='MemberShip start date'),
        ),
    ]
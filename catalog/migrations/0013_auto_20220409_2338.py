# Generated by Django 3.1.7 on 2022-04-09 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20220409_2315'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('can_view_book_instances', 'View book instances'),)},
        ),
    ]

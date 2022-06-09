# Generated by Django 3.1.7 on 2022-06-07 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0026_delete_librarymember'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibraryMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('first_name', models.CharField(max_length=30, verbose_name='Memeber first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Memeber last name')),
                ('membership_start_date', models.DateField(default=django.utils.timezone.now, verbose_name='MemberShip start date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
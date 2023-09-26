# Generated by Django 3.2.20 on 2023-09-25 23:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0016_remove_booking_booking_submitted'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['datetime']},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='time',
        ),
        migrations.AddField(
            model_name='booking',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

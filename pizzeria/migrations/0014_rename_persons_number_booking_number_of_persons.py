# Generated by Django 3.2.20 on 2023-09-15 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0013_remove_booking_booked_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='persons_number',
            new_name='number_of_persons',
        ),
    ]

# Generated by Django 3.2.20 on 2023-09-17 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0014_rename_persons_number_booking_number_of_persons'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_submitted',
            field=models.BooleanField(default=False),
        ),
    ]
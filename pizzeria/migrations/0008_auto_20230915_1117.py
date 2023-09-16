# Generated by Django 3.2.20 on 2023-09-15 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0007_auto_20230915_1045'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['date']},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='date_booked_on',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='time_booked_on',
        ),
        migrations.AddField(
            model_name='booking',
            name='booked_on',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
# Generated by Django 3.2.20 on 2023-09-07 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0004_pizza_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='slug',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='booking',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]

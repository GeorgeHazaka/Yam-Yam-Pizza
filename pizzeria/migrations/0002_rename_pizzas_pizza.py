# Generated by Django 3.2.20 on 2023-07-30 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pizzas',
            new_name='Pizza',
        ),
    ]

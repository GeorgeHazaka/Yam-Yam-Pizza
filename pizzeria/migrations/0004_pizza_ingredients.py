# Generated by Django 3.2.20 on 2023-08-04 20:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pizzeria', '0003_auto_20230731_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='ingredients',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.2.20 on 2023-07-30 16:19

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('persons_number', models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four')], default=1)),
                ('table_number', models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five'), (6, 'Six'), (7, 'Seven'), (8, 'Eight'), (9, 'Nine'), (10, 'Ten'), (11, 'Eleven'), (12, 'Twelve'), (13, 'Thirteen'), (14, 'Fourteen'), (15, 'Fifteen'), (16, 'Sixteen'), (17, 'Seventeen'), (18, 'Eighteen'), (19, 'Nineteen'), (20, 'Twenty')])),
                ('booked_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['booked_on'],
            },
        ),
        migrations.CreateModel(
            name='Pizzas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('price', models.IntegerField()),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
            options={
                'ordering': ['price'],
            },
        ),
    ]

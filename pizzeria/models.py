from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Pizza(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.IntegerField()
    featured_image = CloudinaryField('image', default='placeholder')
    ingredients = models.TextField()

    class Meta:
        ordering = ['price']

    def __str__(self):
        return self.name


AMOUNT_OF_PERSONS = ((1, "One"), (2, "Two"), (3, "Three"), (4, "Four"))
AMOUNT_OF_TABLES = (
    (1, "One"), (2, "Two"), (3, "Three"), (4, "Four"),
    (5, "Five"), (6, "Six"), (7, "Seven"), (8, "Eight"),
    (9, "Nine"), (10, "Ten"), (11, "Eleven"), (12, "Twelve"),
    (13, "Thirteen"), (14, "Fourteen"), (15, "Fifteen"), (16, "Sixteen"),
    (17, "Seventeen"), (18, "Eighteen"), (19, "Nineteen"), (20, "Twenty")
)


class Booking(models.Model):
    username = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    email = models.EmailField()
    persons_number = models.IntegerField(choices=AMOUNT_OF_PERSONS, default=1)
    table_number = models.IntegerField(choices=AMOUNT_OF_TABLES)
    booked_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['booked_on']

    def __str__(self):
        return self.username

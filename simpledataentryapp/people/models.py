from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Person(models.Model):
    # If I recall correctly, these will be required by default since I don't specify otherwise
    # I'm setting arbitrary max lengths
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    # Null=True allows the value to be NULL in DB, blank=True allows the value to be empty in a form
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        # Oldest recorded person was a bit over 122 according to google
        validators=[MinValueValidator(1), MaxValueValidator(123)]
    )
    hometown = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Car(models.Model):
    """car model"""
    TRANSMISSION_CHOISES = [
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
    ]
    title = models.CharField(max_length=100)
    door_num = models.PositiveIntegerField()
    seat_num = models.PositiveIntegerField()
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOISES)
    rating = models.PositiveIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(5),
    ])
    price = models.PositiveIntegerField()
    photo = models.IntegerField()#upload_to='car_photos/', blank=True)

    def __str__(self):
        return self.title
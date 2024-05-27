from django.db.models import TextChoices


class CarChoices(TextChoices):
    Hatchback = 'Hatchback',
    Jeep = 'Jeep',
    Sedan = 'Sedan',
    Bicycle = 'Bicycle',
    Universal = 'Universal',
    Coupe = 'Coupe',
    Wagon = 'Wagon',
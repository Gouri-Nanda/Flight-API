from django.db import models


class Flight(models.Model):
    airline = models.TextField()
    airline_code = models.CharField(max_length=4)
    flight_number = models.CharField(max_length=10)
    origin = models.CharField(max_length=4)
    destination = models.CharField(max_length=4)
    departure_date = models.DateField()
    arrival_date = models.DateField()
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    duration = models.CharField(max_length=10, blank=True, null=True)
    travel_class = models.CharField(max_length=20, blank=True, null=True)
    seats_available = models.IntegerField(blank=True, null=True)
    base_fare = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return f"{self.airline} - {self.flight_number}"


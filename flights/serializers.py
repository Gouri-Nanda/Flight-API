from rest_framework import serializers
from .models import Flight

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ["airline", "airline_code", "flight_number", "origin", "destination", 
                       "departure_date", "arrival_date", "departure_time", "arrival_time", "duration", 
                       "travel_class", "seats_available", "base_fare", "currency"]

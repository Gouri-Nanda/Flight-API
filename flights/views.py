from django.shortcuts import render


# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Flight
from .serializers import FlightSerializer

class FlightInfo(APIView):
    def get(self, request, origin, destination, 
                       departure_date):
        try:
            flight = Flight.objects.filter(origin = origin, destination = destination, departure_date = departure_date)
            serializer = FlightSerializer(flight,many = True)
            return Response(serializer.data)
        except Flight.DoesNotExist:
            return Response({"message": "No Flights available"}, status=status.HTTP_404_NOT_FOUND)
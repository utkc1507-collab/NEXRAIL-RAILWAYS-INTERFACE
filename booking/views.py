from django.shortcuts import render


def home(request):
    return render(request, "booking/home.html")


def trains(request):
    return render(request, "booking/trains.html")


def bookings(request):
    return render(request, "booking/bookings.html")


def stations(request):
    return render(request, "booking/stations.html")
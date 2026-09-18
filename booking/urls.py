from django.urls import path
from . import views

app_name = "booking"

urlpatterns = [
    path("", views.home, name="home"),
    path("trains/", views.trains, name="trains"),
    path("bookings/", views.bookings, name="bookings"),
    path("stations/", views.stations, name="stations"),
]
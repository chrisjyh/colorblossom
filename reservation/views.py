import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from reservation import models


# Create your views here.
def reservationMain(request):
    # reservationList = models.Reservation.objects.all()
    return render(request, "reservation/reservation.html")



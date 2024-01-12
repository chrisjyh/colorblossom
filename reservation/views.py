import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader

from reservation import models


# Create your views here.
def reservationMain(request):
    # reservationList = models.Reservation.objects.all()
    return render(request, "reservation/reservation.html")


def dateSearch(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        response_data = {'status': 'success', 'message': 'Data received successfully.'}
        return JsonResponse(response_data)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

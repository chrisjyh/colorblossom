import json
from datetime import datetime

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader

from accounts.models import ReservationUser
from reservation import models
from reservation.models import ReservationConstraint, Reservation


# Create your views here.
def reservationMain(request):
    # reservationList = models.Reservation.objects.all()
    return render(request, "reservation/reservation.html")


def enrollReservation(request):
    if request.method == 'POST':
        data = request.POST
        userData = ReservationUser()
        resData = Reservation()
        userData.name = data['name']
        userData.email = data['email']
        userData.phone = data['phone']

        resData.user = data['email']
        resData.course = data.get("course")
        resData.reservation_many = data.get("reservation_many")
        resData.reservation_date = data.get("date")
        resData.reservation_hour = data.get("hour")
        resData.reservation_min = data.get("min")
        userData.save()
        resData.save()

        return redirect('askInformationPage')

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def dateSearch(request):
    if request.method == 'POST':
        data = request.POST
        date = datetime.strptime(data.get("date"), '%Y-%m-%d')
        consetraint = models.ReservationConstraint.objects.all().filter(
            start_date__lte=date, end_date__gte=date, type="OPEN"
        )

        dataResult = {
            "workingDay": "open",
            "workingTime": list(consetraint.values("start_time", "end_time")),
            "exceptTime": list("")
        }

        # 영업일이 않일시 closed 반환
        closed = models.ReservationConstraint.objects.all().filter(
            start_date__lte=date, end_date__gte=date, type="CLOSED"
        )
        print(closed)

        if closed.count() < 1:
            response_date = {
                'status': 'success',
                'data': dataResult,
            }
        else:
            response_date = {
                'status': 'success',
                'data': {"workingDay": "closed"}

            }

        return JsonResponse(response_date, safe=False, encoder=DjangoJSONEncoder)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

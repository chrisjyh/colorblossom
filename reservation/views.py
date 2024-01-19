import json
from datetime import datetime, timedelta

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader

from accounts.models import ReservationUser
from reservation import models
from reservation.models import ReservationConstraint, Reservation


# Create your views here.
def reservationMain(request):
    constraintList = ReservationConstraint.objects.all().filter(end_date__gte=datetime.now())

    return render(request, "reservation/reservation.html", {'constraintList' : constraintList})


def enrollReservation(request):
    if request.method == 'POST':
        data = request.POST
        userData = ReservationUser()
        resData = Reservation()

        if ReservationUser.objects.filter(email=data['email']).exists():
            print("Email already registered")
        else:
            userData.name = data['name']
            userData.email = data['email']
            userData.phone = data['phone']
            userData.save()

        resData.user = data['email']
        resData.course = data.get("course")
        resData.reservation_many = data.get("reservation_many")
        resData.reservation_date = data.get("date")
        resData.reservation_hour = data.get("hour")
        resData.reservation_min = data.get("min")
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
        booked_query = models.Reservation.objects.all().filter(reservation_date=date).exclude(status="CANCELLED")

        # 오픈시간 범위
        opening_time = list(consetraint.values("start_time","end_time"))[0]
        # 오픈 하는 시간들 리스트
        opening_time_list = generate_time_intervals(opening_time.get("start_time").strftime('%H:%M'), opening_time.get("end_time").strftime('%H:%M'))
        booked_list = list(booked_query.values("course","reservation_many","reservation_hour","reservation_min"))
        print("opening_time_list--------------------")
        print(opening_time_list)
        print("booked_list--------------------")
        print(booked_list)


        type_consult = {
            # 간단 진단 인당 30분 2인 부터
            "SIMPLE": "00:30",
            # 기본 진단 1인 90분 2인부터 인당 60분
            "BASIC": "01:30",
            "BASICMORE": "01:00",
            # 프로진단 1인 120분
            "PRO": "02:00",
            # 골격 1인 60분
            "BODY": "01:00",
        }

        dataResult = {
            "workingDay": "open",
            "workingTime": list(consetraint.values("start_time", "end_time")),
            "exceptTime": list("")
        }

        # 영업일이 않일시 closed 반환
        closed = models.ReservationConstraint.objects.all().filter(
            start_date__lte=date, end_date__gte=date, type="CLOSED"
        )

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

def generate_time_intervals(start_date,end_date):
    start_time = datetime.strptime(start_date, '%H:%M')
    end_time = datetime.strptime(end_date, '%H:%M')
    interval = timedelta(minutes=30)

    current_time = start_time
    time_intervals = []

    while current_time <= end_time:
        time_intervals.append(current_time.strftime('%H:%M'))
        current_time += interval

    return time_intervals
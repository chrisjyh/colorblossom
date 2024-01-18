from django.http import JsonResponse
from django.shortcuts import render, redirect

from accounts.models import RecommendMarkup, ReservationUser
from reservation.models import Reservation



# Create your views here.

def login_view(request):
    return render(request, 'accounts/login.html')

def loginConfirm(request):
    if request.method == 'GET':
        request.POST.get("email")
        user = ReservationUser.objects.all().filter(email=request.POST.get("email"))
        if user.count() > 0:
            return JsonResponse({'status': 'success', 'data': user})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def myPage(request):
    if request.method == 'GET':
        email = request.GET.get('email')

    user = ReservationUser.objects.all().filter(email=email)
    reservation = Reservation.objects.filter(user=email)

    if user.count() <= 0:
        return redirect("login")

    for e in user:
        if e.consultResult:
            type = list(RecommendMarkup.objects.all().filter(type=str(e.consultResult)).values())
        if e.consultResult02:
            type02 = list(RecommendMarkup.objects.all().filter(type=str(e.consultResult02)).values())

    res_data = list(reservation.values())
    user_data = list(user.values())

    print(res_data)
    print(user_data)
    data = {
        "userName": user_data[0].get("name"),
        "res_data": res_data[0],
        "type": type,
        "type02": type02

    }
    return render(request, 'accounts/mypage.html', {"data": data})

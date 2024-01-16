from django.http import JsonResponse
from django.shortcuts import render, redirect

from accounts import models
from reservation import models


# Create your views here.

def login_view(request):
    return render(request, 'accounts/login.html')

def loginConfirm(request):
    if request.method == 'GET':
        request.POST.get("email")
        user = models.ReservationUser.objects.all().filter(email=request.POST.get("email"))
        if user.count() > 0:
            return JsonResponse({'status': 'success', 'data': user})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def myPage(request):
    if request.method == 'GET':
        email = request.GET.get('email')

    user = models.ReservationUser.objects.all().filter(email=email)

    for e in user:
        print(str(e.consultResult))
        print(str(e.consultResult02))

    print(user)
    data = {
        "user": user,
        "message": "You have successfully logged",
        "status": "success"
    }
    return render(request, 'accounts/mypage.html', {"data": data})

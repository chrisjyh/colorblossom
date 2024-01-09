from django.shortcuts import render
from . import models
from .models import AskInformation


# Create your views here.
def faqTemplate(request):
    faqList = models.Faq.objects.all().filter(useyn=True)
    return render(request, "faq/faq.html", {'faqPost': faqList})

def askInformation(request):
    askList = models.AskInformation.objects.all().filter(use_yn=True)
    for ask in askList:
        askLabel = get_status_display(ask.status)
        ask.askLabel = askLabel
    return render(request, "faq/community.html", {'askList': askList})

def get_status_display(req):
    if req == "P" or req =="p":
        return "결제/예약"
    elif req == "A":
        return "상담"
    else:
        return "기타"

def askform(request):
    return None

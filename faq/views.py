from django.shortcuts import render
from . import models


# Create your views here.
def faqTemplate(request):
    faqList = models.Faq.objects.all().filter(useyn=True)
    return render(request, "faq/faq.html", {'faqPost': faqList})


def askInformation(request):
    return render(request, "faq/community.html")


def askform(request):
    return None

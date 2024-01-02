import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('reservation/reservation.html')
    context = {
        'currnet_date': "now"
    }
    return HttpResponse(template.render(context, request) )
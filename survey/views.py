from django.shortcuts import render
from django.db.models.query import QuerySet
from django.http import HttpResponse
from survey.models import Survey, Question, Choice, Result

# Create your views here

def survey_view(request):
    queryset = Survey.objects.select_related
    print(queryset)
    data = ""
    return render(request, "survey/survey.html",{
        "data": data,
    })

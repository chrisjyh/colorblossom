from django.shortcuts import render

# Create your views here.
def selftest(request):
    return render(request, "selftest/selftest.html")
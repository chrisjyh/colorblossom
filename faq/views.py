from django.shortcuts import render


# Create your views here.
def faqTemplate(request):
    return render(request, "faq/faq.html")

def askInformation(request):
    return render(request, "faq/community.html")
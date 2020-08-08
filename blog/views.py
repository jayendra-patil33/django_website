from django.shortcuts import render


# Create your views here.
def home(request):

    return render( request, "blog/index.html",)

def ourSponsors(request):
    return render(request, "blog/ourSponsors.html")

def ourJourney(request):
    return render(request, "blog/ourJourney.html")

def aboutUs(request):
    return render(request, "blog/aboutUs.html")
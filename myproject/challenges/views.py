from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Welcome to the January challenge",
    "february": "Welcome to the February challenge",
    "march": "Welcome to the March challenge",
    "april": "Welcome to the April challenge",
    "may": "Welcome to the May challenge",
    "june": "Welcome to the June challenge",
    "july": "Welcome to the July challenge",
    "august": "Welcome to the August challenge",
    "september": "Welcome to the September challenge",
    "october": "Welcome to the October challenge",
    "november": "Welcome to the November challenge",
    "december": "Welcome to the December challenge"
}
# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        return HttpResponseNotFound("<h1>Plase enter a valid month</h1>")
    

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("Plase enter a valid month")
    return HttpResponse(challenge_text)


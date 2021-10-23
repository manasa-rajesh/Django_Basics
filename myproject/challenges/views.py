from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    if month == 'january':
        return HttpResponse("Welcomw to January")
    elif month == 'february':
        return HttpResponse("Welcomw to February")
    elif month == 'march':
        return HttpResponse("Welcomw to March")
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)


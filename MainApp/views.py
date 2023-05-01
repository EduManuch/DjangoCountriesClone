from django.shortcuts import render
import json
from django.http import HttpResponse

with open("countries.json", 'r') as f:
    countries = json.load(f)


def home(request):
    # return HttpResponse("<h2>Hello!!!</h2>")
    context = {'name': "HELLO WORLD !"}
    return render(request, 'index.html', context)


def countries_list(request):
    context = {'countries': countries}
    return render(request, 'countries-list.html', context)


def country_page(request, country):
    for item in countries:
        if item['country'] == country:
            context = {'country': country,
                       'languages': item['languages']}
            return render(request, 'country-page.html', context)

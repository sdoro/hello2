from django.shortcuts import render

# Create your views here.
from pif import get_public_ip
from django.http import HttpResponse

def myIp(request):
    ip = get_public_ip()
    html = "<html><body>Welcome, my IP is: " + ip + "</body></html>"
    return HttpResponse(html)

import time
from datetime import date
from django.shortcuts import render

def year(request):
    oggi = date.today()
    ip = get_public_ip()
    tmp = {'title': oggi, 'h1': 'year: ' + str(oggi.year), 'p': ip}
    return render(request, 'estesa.html', {'terna': tmp})

def month(request):
    oggi = date.today()
    ip = get_public_ip()
    tmp = {'title': oggi, 'h1': "month: " + str(oggi.month), 'p': ip}
    return render(request, 'estesa.html', {'terna': tmp})

def day(request):
    oggi = date.today()
    ip = get_public_ip()
    tmp = {'title': oggi, 'h1': "day: " + str(oggi.day), 'p': ip}
    return render(request, 'estesa.html', {'terna': tmp})

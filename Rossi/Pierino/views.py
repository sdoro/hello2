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
    var = {'data': oggi, 'tempo': oggi.year, 'ip': ip}
    return render(request, 'estesa.html', {'section': var})

def month(request):
    oggi = date.today()
    ip = get_public_ip()
    var = {'data': oggi, 'tempo': oggi.month, 'ip': ip}
    return render(request, 'estesa.html', {'section': var})

def day(request):
    oggi = date.today()
    ip = get_public_ip()
    var = {'data': oggi, 'tempo': oggi.day, 'ip': ip}
    return render(request, 'estesa.html', {'section': var})

from pif import get_public_ip
from django.http import HttpResponse

def myIp(request):
    ip = get_public_ip()
    html = "<html><body>Welcome, my IP is: " + ip + "</body></html>"
    return HttpResponse(html)

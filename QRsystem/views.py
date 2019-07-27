from django.shortcuts import render
import pyqrcode
from .models import QRcode
# Create your views here.

def page_a(request):
    url = pyqrcode.create('http://uca.edu')
    url.svg('uca-url.svg', scale=8)

    print(url.terminal(quiet_zone=1))
    site_address = QRcode.objects.filter(url='www.onsot.kr')[0]
    return render(request, 'QRsystem/Apage.html', {'site_address' : site_address})


def page_b(request):
    pass
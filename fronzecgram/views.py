"""Vistas de nuestra aplicacion"""
import json
from django.http import HttpResponse
from datetime import datetime


def hola_mundo(request):
    """Return a greeting"""
    now  = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Server time is {now}'.format(now=str(now)))


def hi(request):
    """Hi"""
    numbers = request.GET['numbers']    
    return HttpResponse(json.dumps(sorted([int(x) for x in numbers.split(',')])))
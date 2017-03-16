from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

def uist(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'uist.html')


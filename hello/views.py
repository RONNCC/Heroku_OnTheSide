from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

def uist(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'uist.html')

def aug14(request):
    return render(request, 'aug14.html')
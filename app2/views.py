from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def manju(request):
    return HttpResponse('manju is a good girl')



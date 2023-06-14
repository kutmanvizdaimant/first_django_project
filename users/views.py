from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    b = 23 + 27
    return HttpResponse(f'Hello my name is Kutman  {b}')
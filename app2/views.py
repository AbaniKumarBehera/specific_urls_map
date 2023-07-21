from django.shortcuts import render
from django.http import HttpResponse


def  second(request):
    return HttpResponse('<h1>what is this</h2>')



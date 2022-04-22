from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    return HttpResponse('apel')
from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1> Caballero esa utilizando django</h1>")
def about(request):
    return HttpResponse('Eres un Imbecil .l.')
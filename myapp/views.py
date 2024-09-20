from django.shortcuts import render
from django.http import HttpResponse

def  index(request):
    return HttpResponse("pagina del index ")




def inicio(request, username):
    print(username)  # Imprimirá el username en la consola
    return HttpResponse(f"<h1> Caballero, está utilizando Django. Prueba de parámetros: {username}</h1>")  # Muestra el username

def about(request):
    return HttpResponse('Esta es la página de "Acerca de".')

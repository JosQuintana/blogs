from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.shortcuts import HttpResponse, redirect

def index(request):
    objeto ={"titulo": "Jose"};
    return JsonResponse(objeto)

def root(request):
    return HttpResponse("Hola desde root")

def redirige(request):
    return redirect("blogs")

def new(request):
    return HttpResponse("placehlpder para mostrar un nuevo formulario en el blog")

def edit(request, numero):
    return HttpResponse(f"placeholder para editar el blog {numero}")
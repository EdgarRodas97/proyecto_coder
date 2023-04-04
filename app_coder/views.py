from django.shortcuts import render
from .models import CursoChirho
from django.http import HttpResponse

# Create your views here.
def crear_curso_chirho(request):

    nombre_curso_chirho="python"
    comision_curso_chirho="51325"

    curso_chirho=CursoChirho(nombre_chirho=nombre_curso_chirho, comision_chirho=comision_curso_chirho)
    curso_chirho.save()
    respuesta_chirho=f"Curso creado --- {nombre_curso_chirho} - {comision_curso_chirho}"
    return HttpResponse(respuesta_chirho)    

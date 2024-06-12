from django.shortcuts import render


def principal(request):
    return render(request,"inicio/principal.html")

# Create your views here.
def cursos(request):
    return render(request,"inicio/cursos.html")

def contacto(request):
    return render(request,"inicio/contacto.html")   
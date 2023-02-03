from django.http import HttpResponse

def saludo(request): #primera vista

    return HttpResponse("Bienvenidxs!")
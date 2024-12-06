from django.shortcuts import render, redirect
from .models import Libro
from django.core.mail import send_mail

from django.conf import settings
def lista_libros(request):
    libros = Libro.objects.all()
    query = request.GET.get('q')
    if query:
        libros = libros.filter(titulo__icontains=query)
    return render(request, 'lista_libros.html', {'libros': libros})

def agregar_libro(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        publicacion = request.POST['publicacion']
        genero = request.POST['genero']
        Libro.objects.create(
            titulo=titulo, autor=autor, publicacion=publicacion, genero=genero
        )
        return redirect('lista_libros')
    return render(request, 'agregar_libro.html')


def enviar_correo(request):
    # Parámetros del correo
    asunto = 'Asunto del correo'
    cuerpo = 'Este es el cuerpo del correo.'
    remitente = settings.DEFAULT_FROM_EMAIL 
    destinatario = ['kimberly.gomezvelazquez@cesunbc.edu.mx']  

    try:
        # Intento enviar correo
        send_mail(asunto, cuerpo, remitente, destinatario, fail_silently=False)
        return render(request, 'correo_enviado.html')  
    except Exception as e:
        print(f'Error al enviar el correo: {e}')
        return render(request, 'error_correo.html')  

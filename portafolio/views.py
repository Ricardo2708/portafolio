from django.shortcuts import render, get_object_or_404, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
import requests
from .models import Proyectos, Noticias, Suscripciones
from .forms import FormContacto
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    proyectos = Proyectos.objects.all().order_by('-id')
    noticias = Noticias.objects.all().order_by('-id')
    return render(request, 'index.html', {
        'title':'Inicio',
        'proyectos':  proyectos,
        'noticias': noticias
    })

def ultimas__noticias(request, slug=""):
    noticia = get_object_or_404(Noticias, slug_noticia = slug)
    return render(request, "pages/custom/custom.html",{
        'title': noticia.subnombre_noticia,
        'noticia': noticia
    })

def formulario(request):
    if request.method == 'POST':
        formulario = FormContacto(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data

            nombre = data_form.get('nombre')
            email = data_form.get('correo')
            servicios = data_form.get('servicios')
            mensaje = data_form.get('mensaje')

             # Verifica el reCAPTCHA utilizando la API de Google
            recaptcha_response = request.POST.get('g-recaptcha-response')
            recaptcha_secret_key = settings.RECAPTCHA_PRIVATE_KEY

            recaptcha_data = {
                'secret': recaptcha_secret_key,
                'response': recaptcha_response,
            }

            response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=recaptcha_data)
            result = response.json()


            if not result['success']:
                messages.error(request, 'Recaptcha No Valido',extra_tags='errorForm')
                return redirect('inicio')
            
            else:
                template = render_to_string('pages/email/email.html',{
                    'nombre': nombre,
                    'email': email,
                    'servicios': servicios,
                    'mensaje': mensaje
                })

                email = EmailMessage(
                    f"{nombre} - {servicios}",
                    template,
                    settings.EMAIL_HOST_USER,
                    ['vegaricardo636@gmail.com']
                )

                email.fail_silently = False
                email.send()

                messages.success(request, 'Formulario Enviado',extra_tags='successForm')
                return redirect('inicio')
        
        messages.error(request, 'Se Produjo Un Error',extra_tags='errorForm')
        return redirect('inicio')
    
    return redirect('inicio')

def newsletter_form(request):
    if request.method == 'POST':
        email = request.POST.get('email').lower() 

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, 'La dirección de correo electrónico no es válida', extra_tags='newsletterForm')
            return redirect('inicio')
    
        suscripciones = Suscripciones(
            email_suscripcion = email
        )
        suscripciones.save()

        messages.success(request, 'Gracias Por Suscribirte',extra_tags='newsletterForm')
        return redirect('inicio')

    return redirect('inicio') 
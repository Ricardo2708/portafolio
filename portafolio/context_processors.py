from .models import Proyectos, Noticias
from .forms import FormContacto

def get_formulario(request):
    formulario = FormContacto()
    return{
        'form': formulario
    }


def get_proyectos(request):
        proyectos_nav = Proyectos.objects.all().order_by('-id')[:5]
        return{
            'proyectos_nav' : proyectos_nav,
        }

def get_noticias(request):
        noticias_nav = Noticias.objects.all().order_by('-id')[:5]
        return{
            'noticias_nav' : noticias_nav
        }
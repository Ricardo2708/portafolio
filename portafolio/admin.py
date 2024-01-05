from django.contrib import admin
from .models import Lenguajes, Proyectos, Noticias, Suscripciones
# Register your models here.
class LenguajesAdmin(admin.ModelAdmin):
    search_fields=('nombre_lenguaje', 'categoria')
    list_filter=('created_at','updated_at')
    list_per_page = 15
    date_hierarchy= 'created_at'
    list_display=( 
        'nombre_lenguaje',
        'categoria',
        'created_at',
    )


class ProyectosAdmin(admin.ModelAdmin):
    search_fields=('nombre_proyecto', 'tags_proyecto')
    list_filter=('created_at','updated_at')
    list_per_page = 15
    date_hierarchy= 'created_at'
    list_display=( 
        'nombre_proyecto',
        'created_at',
        'url_proyecto',
        'url_github',
     )
    
class NoticiasAdmin(admin.ModelAdmin):
    readonly_fields = ('slug_noticia', )
    search_fields=('nombre_noticia', 'subnombre_noticia')
    list_filter=('created_at','updated_at')
    list_per_page = 15
    date_hierarchy= 'created_at'
    list_display=( 
        'nombre_noticia',
        'subnombre_noticia',
        'created_at',
    )
    
class SuscripcionesAdmin(admin.ModelAdmin):
    search_fields=('email_suscripcion',)
    list_filter=('created_at','updated_at')
    list_per_page = 15
    date_hierarchy= 'created_at'
    list_display=( 
        'email_suscripcion',
        'updated_at',
        'created_at',
    )

admin.site.register(Lenguajes, LenguajesAdmin)
admin.site.register(Proyectos, ProyectosAdmin)
admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Suscripciones, SuscripcionesAdmin)

#Configuracion Del Panel
title = "Administracion"
subtitle = "Administracion"

admin.site.site_header =  title
admin.site.site_title = title
admin.site.index_title = subtitle
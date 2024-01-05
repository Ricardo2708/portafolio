from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

CATEGORIA ={
    ('FrontEnd', 'FrontEnd'),
    ('BackEnd', 'BackEnd'),
    ('FullStack', 'FullStack'),
}

class Lenguajes(models.Model):
    nombre_lenguaje = models.CharField(max_length=60, verbose_name='Nombre:', default='')
    categoria = models.CharField(max_length=100, verbose_name="Categoria:", choices=CATEGORIA, default='none')   
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El :')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El :')

    class Meta:
        verbose_name = "Lenguaje"
        verbose_name_plural = "Lenguajes"

    def clean(self):
        self.nombre_lenguaje = self.nombre_lenguaje.lower() 

    def __str__(self):
        return f'{self.nombre_lenguaje}  | {self.categoria}'

class Proyectos(models.Model):
    nombre_proyecto = models.CharField(max_length=60, verbose_name='Nombre:', default='')
    tags_proyecto = models.ManyToManyField(Lenguajes, verbose_name="Tags:",related_name='opcion1', default='')
    image_proyecto = models.ImageField(upload_to='proyects_images/', blank=True, null=True)
    descripcion_proyecto = models.TextField(verbose_name='Descripcion', default='')
    url_proyecto = models.CharField(max_length=100, verbose_name='URL:', default='')
    url_github = models.CharField(max_length=100, verbose_name='Github:', default='')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El :')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El :')

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return f'{self.nombre_proyecto}  | {self.url_proyecto}'
    
class Noticias(models.Model):
    nombre_noticia = models.CharField(max_length=60, verbose_name='Nombre:', default='')
    subnombre_noticia = models.CharField(max_length=60, verbose_name='Subnombre:', default='')
    autor_noticia = models.CharField(max_length=60, verbose_name='Autor:', default='')
    slug_noticia = models.CharField(max_length=60, verbose_name='Url Amigable:', default='', editable=False)
    image_noticia = models.ImageField(upload_to='news_images/', blank=True, null=True)
    text = CKEditor5Field('Text', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El :')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El :')

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"

    def clean(self):
        url = self.subnombre_noticia.lower()  
        self.slug_noticia = url.replace(" ", "-")

    def __str__(self):
        return f'{self.nombre_noticia}  | {self.subnombre_noticia}'
    

class Suscripciones(models.Model):
    email_suscripcion = models.CharField(max_length=60, verbose_name='Correo:', default='')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado El :')
    updated_at = models.DateTimeField(auto_now =True, verbose_name='Actualizado El :')

    class Meta:
        verbose_name = "Suscripcion"
        verbose_name_plural = "Suscripciones"

    def __str__(self):
        return f'{self.email_suscripcion}'
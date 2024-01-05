# Generated by Django 4.2.6 on 2023-11-10 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0006_noticias_slug_noticia_alter_lenguajes_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticias',
            name='autor_noticia',
            field=models.CharField(default='', max_length=60, verbose_name='Autor:'),
        ),
        migrations.AlterField(
            model_name='lenguajes',
            name='categoria',
            field=models.CharField(choices=[('FullStack', 'FullStack'), ('BackEnd', 'BackEnd'), ('FrontEnd', 'FrontEnd')], default='none', max_length=100, verbose_name='Categoria:'),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='slug_noticia',
            field=models.CharField(default='', editable=False, max_length=60, verbose_name='Url Amigable:'),
        ),
    ]

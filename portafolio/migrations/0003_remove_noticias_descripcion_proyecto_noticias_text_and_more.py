# Generated by Django 4.2.6 on 2023-11-09 22:41

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0002_noticias_alter_lenguajes_categoria_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticias',
            name='descripcion_proyecto',
        ),
        migrations.AddField(
            model_name='noticias',
            name='text',
            field=django_ckeditor_5.fields.CKEditor5Field(default=1, verbose_name='Text'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='noticias',
            name='subnombre_noticia',
            field=models.CharField(default='', max_length=60, verbose_name='Subnombre:'),
        ),
    ]
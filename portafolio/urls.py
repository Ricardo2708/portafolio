from django.urls import path
from portafolio import views

urlpatterns=[
    path('', views.index, name="inicio"),
    path('noticias/<str:slug>', views.ultimas__noticias, name="noticias"),
    path('formulario/', views.formulario, name="formulario"),
    path('newsletter/', views.newsletter_form, name="newsletter")
]
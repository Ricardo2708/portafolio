from django import forms


class FormContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'placeholder': '*Ingrese su nombre'}))
    correo = forms.CharField(label="Correo", widget=forms.TextInput(attrs={'placeholder': '*Ingrese su correo'}))


    opciones_developer =[
        ('Desarrollo Web', 'Desarrollo Web'),
        ('Diseños & Mas', 'Diseños & Mas'),
        ('Marketing Online', 'Marketing Online'),
        ('Otros', 'Otros'),
    ]

    servicios = forms.TypedChoiceField(label="Servicios", choices= opciones_developer)
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Quita las etiquetas de los campos del formulario
        self.fields['nombre'].label = False
        self.fields['correo'].label = False
        self.fields['servicios'].label = False
        self.fields['mensaje'].label = False

# -*- coding: utf-8 -*-
from django import forms

import account.forms


class SignupForm(account.forms.SignupForm):
    choices = [('Participante', 'Participante / Assistant'),
               ('Doctorando', 'Doctorando / Phd student'),
               ('Estudiante', 'Estudiante / Undergraduate student')]
    first_name = forms.CharField(label='Nombre / First Name')
    last_name = forms.CharField(label='Apellido / Last Name')
    email_confirm = forms.EmailField(label="Confirmar Email / Confirm email")
    dni = forms.CharField(label="Documento / Document Number")
    direccion = forms.CharField(label=u"Dirección / Address", required=False)
    localidad = forms.CharField(label="Localidad / City", required=False)
    provincia = forms.CharField(label="Provincia / State", required=False)
    pais = forms.CharField(label="Pais / Country")
    institucion = forms.CharField(label="Institución o Empresa / Institution or Company")
    categoria = forms.ChoiceField(label="Categoria / Category", choices=choices)


    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        del self.fields["username"]
        self.fields.keyOrder = [
            "email",
            "email_confirm",
            "first_name",
            "last_name",
            "password",
            "password_confirm",
            "dni",
            "direccion",
            "localidad",
            "provincia",
            "pais",
            "institucion",
            "categoria"
        ]

    def clean_email_confirm(self):
        email = self.cleaned_data.get("email")
        email_confirm = self.cleaned_data["email_confirm"]
        if email:
            if email != email_confirm:
                raise forms.ValidationError("Los emails no coinciden")
        return email_confirm

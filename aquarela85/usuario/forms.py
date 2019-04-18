# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class UserModelForm(forms.ModelForm):
    def save(self, commit=True):
        user = super(UserModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

        return user

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome',
                'required': True,
                'maxlength': 15
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sobrenome',
                'required': True,
                'maxlength': 15
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'required': True,
                'maxlength': 100
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Usuário',
                'required': True,
                'maxlength': 50
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Senha',
                'required': True,
                'maxlength': 50
            }),
        }

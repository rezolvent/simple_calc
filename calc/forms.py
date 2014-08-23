# -*- coding:utf-8 -*-
from django import forms


class ContactForm(forms.Form):
    email_from = forms.EmailField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': "E-mail"}),
        required=True)
    email_to = forms.EmailField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': "E-mail"}),
        required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': "Пароль"}),
        required=True)

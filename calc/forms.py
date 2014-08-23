# -*- coding:utf-8 -*-
from django import forms


class ContactForm(forms.Form):
    email_from = forms.EmailField(required=True)
    email_to = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, query_dict=None):
        if query_dict is None:
            items = query_dict
        else:
            items = dict()
            for key in self.base_fields.keys():
                items[key] = query_dict.getlist(key)[0]
        forms.Form.__init__(self, items)

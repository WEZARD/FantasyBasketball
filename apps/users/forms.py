# -*- coding: utf-8 -*-
__author__ = 'zx'
__date__ = '08/05/2017 03:31'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

# -*- coding: utf-8 -*-
from django import forms
# from captcha.fields import CaptchaField

__author__ = 'zx'
__date__ = '08/05/2017 03:31'


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    # captcha = CaptchaField(error_messages={'invalid': u'Invalid verify code!'})

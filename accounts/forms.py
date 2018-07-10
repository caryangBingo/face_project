#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caryangBingo
# @Date:   2018-07-10 10:27:29
# @Software : Sublime Text3
# @File Name:   forms.py
# @Last Modified time: 2018-07-10 10:40:05

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """docstring for SignUpForm"""
    email = forms.CharField(max_length=254, required=True,
                            widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caryangBingo
# @Date:   2018-07-06 14:46:08
# @Software : Sublime Text3
# @File Name:   forms.py
# @Last Modified time: 2018-07-06 14:50:38

from django import forms
from .models import Topic


class NewTopicForm(forms.ModelForm):
    message=forms.CharField(widget=forms.Textarea(),max_length=4000)

    class Meta:
        model=Topic
        fields=['subject','message']

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: caryangBingo
# @Date:   2018-07-06 14:46:08
# @Software : Sublime Text3
# @File Name:   forms.py
# @Last Modified time: 2018-07-08 13:46:47

from django import forms
from .models import Topic


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your  mind?'}),
        max_length=4000,
        help_text='The max length of the text is 4000.')

    class Meta:
        model = Topic
        fields = ['subject', 'message']

from .models import *
from django.db import models
from django import forms

from django.forms import ModelForm

class ValueForm(ModelForm):
    class Meta:
        model = Value
        fields = ['value_name', 'related_feature_name']

class FeatureForm(ModelForm):
    class Meta:
        model = Feature
        fields = ['feature_name','values']
        # values = forms.ModelChoiceField(queryset=Value.objects.filter(related_feature_name = 'test'), label='value', widget=forms.Select)

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['tag_name']
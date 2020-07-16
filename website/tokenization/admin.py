from django.contrib import admin
from .models import *
from .forms import *


class ValueAdmin(admin.ModelAdmin):
    list_display = ['value_name', 'related_feature_name']
    form = ValueForm
    list_filter = ['value_name','related_feature_name']
    search_fields = ['value_name','related_feature_name']

class FeatureAdmin(admin.ModelAdmin):
    list_display = ['feature_name']
    form = FeatureForm
    list_filter = ['feature_name']
    search_fields = ['feature_name']
# Register your models here.

admin.site.register(Value, ValueAdmin) #customization on Value model
admin.site.register(Feature, FeatureAdmin) #customization on Feature model
admin.site.register(Tag)

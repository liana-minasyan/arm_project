from django.shortcuts import render, redirect
from django.http import  HttpResponse
from .forms import *
# Create your views here.
def home(request):
     return render(request, 'base.html')

def edit(request):
    return render(request, 'edit.html')

def dashboard(request):
    title = 'Welcome to our awesome page'
    form = FeatureForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form.save_m2m()
        return redirect('/dashboard')
    context = {
        'title': title,
        'form': form,
    }
    return render(request, 'dashboard.html', context)
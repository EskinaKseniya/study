from django.shortcuts import render, redirect
from myapp.form import AddPatient
from myapp.models import *
from django.views.generic import ListView, DetailView


# Create your views here.

class PatientListView(ListView):
    model = Patient
    template_name = 'medical/index.html'

class AboutPatient(DetailView):
    model = Patient
    template_name = 'medical/aboutPatient.html'

def addPatient(request):
    if request.method == 'POST':
        form = AddPatient(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPatient()
    return render(request, 'medical/form.html', {'form': form})

from django.shortcuts import render, redirect
from myapp.form import AddPatient
from myapp.models import *
from django.views.generic import ListView, DetailView, UpdateView


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

def changePatient(request):
    if request.method == 'POST':
        form = AddPatient(request.Post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPatient()
    return render(request, 'medical/changePatient.html', {'form': form})
class PatientChangeListView(ListView):
    model = Patient
    template_name = 'medical/changedata.html'

class ChangePatient(UpdateView):
    model = Patient
    template_name = 'medical/changePatient.html'
    fields = ['first_name', 'last_name', 'age', 'diagnosis', 'doctor', 'room']
from django import forms
from .models import Patient

class AddPatient(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'age', 'diagnosis', 'doctor', 'room']


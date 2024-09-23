# forms.py
from django import forms
from .models import CourseForm

class CourseFormForm(forms.ModelForm):
    class Meta:
        model = CourseForm
        fields = ['name', 'surname', 'phone_number', 'phon1']

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import ClassAssignment

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RosterUploadForm(ModelForm):
    user = 
    period1file = forms.FileField(label="File for Period 1")
    period2file = forms.FileField(label="File for Period 2")
    period3file = forms.FileField(label="File for Period 3")
    period4file = forms.FileField(label="File for Period 4")
    period6file = forms.FileField(label="File for Period 6")
    period7file = forms.FileField(label="File for Period 7")
    period8file = forms.FileField(label="File for Period 8")

    class Meta:
        model = ClassAssignment
        fields=['period1file', 'period2file', 'period3file', 'period4file', 'period6file', 'period7file', 'period8file']
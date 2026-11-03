from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "email", "age"]

# class ClacForm(forms.Form):
#     a = forms.FloatField(label="a")
#     b = forms.FloatField(label="b")
#     symbol_math = forms.FloatField(label="symbol")
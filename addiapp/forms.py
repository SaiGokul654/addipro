from django import forms

class AdditionForm(forms.Form):
    num1 = forms.IntegerField(label="Enter first number")
    num2 = forms.IntegerField(label="Enter second number")

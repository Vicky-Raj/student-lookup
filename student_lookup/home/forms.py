from django import forms

class StduentForm(forms.Form):
    name = forms.CharField(max_length=20)
    registerNo = forms.CharField(max_length=10)
    department = forms.CharField(max_length=10)
    room = forms.CharField(max_length=8)
    batch = forms.CharField(max_length=5)
    parentNo = forms.CharField(max_length=10)
    studentNo = forms.CharField(max_length=10)
    image = forms.ImageField()    

from django import forms

class UserRegisterForm(forms.Form):
    Directory = forms.CharField(label = 'Directory',max_length = 200)
    Name = forms.CharField(label='Name',max_length=100)
    Email = forms.CharField(label='Email',max_length=100)
    Username = forms.CharField(label='Username',max_length=20)
    Password = forms.CharField(label='Password',max_length=100)
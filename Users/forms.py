from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':('Username')})
        self.fields['email'].widget.attrs.update({'placeholder':('Email')})
        self.fields['password1'].widget.attrs.update({'placeholder':('Password')})        
        self.fields['password2'].widget.attrs.update({'placeholder':('Confirm password')})

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
class UserUpdateFrom(forms.ModelForm):
     email = forms.EmailField()

     class Meta:
        model = User
        fields = ['username','email']            

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class NameForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ['first_name', 'last_name']

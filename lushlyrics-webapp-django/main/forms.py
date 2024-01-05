from django import forms
from .models import playlist_user

class SignUpForm(forms.ModelForm):
    class Meta:
        model = playlist_user
        fields = ['username', 'email', 'password'] 
        widgets = {
            'password': forms.PasswordInput(),
        }
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLES)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'role')
        
class MyForm(forms.Form):
    field1 = forms.CharField(max_length=100)
    field2 = forms.IntegerField()

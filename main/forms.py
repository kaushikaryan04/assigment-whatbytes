from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


class CustomUserCreationForm(UserCreationForm) :
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    def save(self ,comit = True) :
        user = super().save(commit= False)
        user.email = self.cleaned_data['email']

        if comit :
            user.save() 
        return user


    class Meta :

        model = User 
        fields = ['username' , 'email' , 'password1' , 'password2']



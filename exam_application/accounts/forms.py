
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from django.forms import fields


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        error_messages = {
            'password_missmatch': _('Паролите не съвпадат'),
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Потребителско име'
        self.fields['email'].label = 'Имейл'
        self.fields['password1'].label = 'Парола'
        self.fields['password2'].label = 'Повтори паролата'

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'Паролите не съвпадат')

        return password2

    

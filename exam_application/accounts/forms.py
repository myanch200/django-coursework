
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from django.forms import fields
"""
във този файл се намират всички наши форми във повечето случаи отново използваме наследяването, 
за да можем да наследим куп атрибути и функционалности от джанго класове

"""

# В този случаи имаме регистрационна форма, която наследява атрибути и функционалност от UserCreationForm
class UserRegistrationForm(UserCreationForm):
  # в класа мета описваме кой е моделът върху който формата ще се изпълни кои полета са ни нужни и можем да правим 
  # много различни неща като да зададем собствени съобщения при случай на грешка
    class Meta:
        model = User
        fields = ("first_name", "last_name",
                  "email", "username", "password1", "password2")
        error_messages = {
            'password_missmatch': _('Паролите не съвпадат'),
        }

    # тук определяме неща като какво вид html да използва за всяко от полета на този модел
    # можем да зададем и наши преводи на имената на тези полета
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = 'Първо име'
        self.fields['last_name'].label = 'Фамилия'
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

# Профил формата наследява от ModelForm,което ни дава достъп до какви полета да има и какъв ще е моделът отново
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Потребителско име'
        self.fields['email'].label = 'Имейл'
        self.fields['first_name'].label = 'Първо име'
        self.fields['last_name'].label = 'Фамилия'
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'w-full px-4 py-2'})
        self.help_text = ''




    

    

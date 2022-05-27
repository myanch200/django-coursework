from django import forms
from modules.models import Module
from django.contrib.auth.models import User

# Тук създаваме формата за добавяне на нов модул или курс 
# отново наследяваме от forms.ModelForm и определяме както  модела така и полетата които искаме да включим във формата
class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'description','participants']

    participants = forms.ModelMultipleChoiceField(
      # all users that are not superusers
        queryset= User.objects.filter(is_superuser=False), # Казваме как да изберем всички потребители които не са супер администратори и за всяко да checkbox
        widget=forms.CheckboxSelectMultiple # Тъй като един курс може да има много студенти така и много студенти могат да бъдат в много курсове връзката междъ тях е many to many
        # Затова използвам checkbox , с който да определим дали потребителя ще участва в този курс

    )
    
    def __init__(self, *args, **kwargs):
        super(ModuleForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'p-3'
        self.fields['name'].label = 'Име на специалността'
        self.fields['description'].label = 'Описание'
        self.fields['participants'].label = 'Студенти'
        self.fields['participants'].required = False





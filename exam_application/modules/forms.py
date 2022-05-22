from django import forms
from modules.models import Module
from django.contrib.auth.models import User
class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'description','participants']

    participants = forms.ModelMultipleChoiceField(
      # all users that are not superusers
        queryset= User.objects.filter(is_superuser=False),
        widget=forms.CheckboxSelectMultiple
    )
    
    def __init__(self, *args, **kwargs):
        super(ModuleForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'p-3'
        self.fields['name'].label = 'Име на специалността'
        self.fields['description'].label = 'Описание'
        self.fields['participants'].label = 'Студенти'




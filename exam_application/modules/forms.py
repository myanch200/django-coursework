from django import forms
from modules.models import Module

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'description']
    
    def __init__(self, *args, **kwargs):
        super(ModuleForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'p-3'
        self.fields['name'].label = 'Име на специалността'
        self.fields['description'].label = 'Описание'


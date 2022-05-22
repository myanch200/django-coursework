from django import forms

from modules.models import  Exam

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['name', 'description', 'exam_date']
    
    def __init__(self, *args, **kwargs):
        self.fields['name'].label = 'Име на изпита'
        self.fields['description'].label = 'Описание'
        self.fields['exam_date'].label = 'Дата и час на изпита'
        super(ExamForm, self).__init__(*args, **kwargs)
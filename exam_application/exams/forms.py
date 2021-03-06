from django import forms

from modules.models import  Exam
# Тук отново имаме ModelForm този път за изпит
class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ('name', 'description', 'exam_date')
        """
        определяме какъв елемнт ше се визуализира за атрибута exam_date  на този изпит, 
        в нашия случай искаме поле, с което да изберем дата и час
        """
        widgets = {
            'exam_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
    
    def __init__(self, *args, **kwargs):
        super(ExamForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Име на изпита'
        self.fields['description'].label = 'Описание'
        self.fields['exam_date'].label = 'Дата и час на изпита'
        # make exam_date field a date picker

        self.fields['exam_date'].widget
from django import template
from django.contrib.auth.models import User
from modules.models import  Exam
register = template.Library()

@register.filter(name='exam_params')
def exam_params(user_id, exam_id):
   user = User.objects.get(id=user_id)
   exam = Exam.objects.get(id=exam_id)   
   return user.is_registered_for_exam(exam)
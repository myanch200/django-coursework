"""
Отново тъй като django template engine не приема параметри при извикване то на функции
 ни се налага да си създададем собствени тагове, които да го правят за нас
"""


from django import template
from django.contrib.auth.models import User
from modules.models import  Exam
register = template.Library()

@register.filter(name='exam_params')
def exam_params(user_id, exam_id):
   user = User.objects.get(id=user_id)
   exam = Exam.objects.get(id=exam_id)   
   return user.is_registered_for_exam(exam)
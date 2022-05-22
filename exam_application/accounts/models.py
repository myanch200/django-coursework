from django.db import models
from django.contrib import auth

def is_registered_for_exam(self,exam):
    return self.exam_applications.filter(exam=exam).exists()


auth.models.User.add_to_class('is_registered_for_exam', is_registered_for_exam)

# Create your models here.


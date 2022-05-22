from django.urls import path
from . import views
app_name = "exams"

urlpatterns = [
  path('exam-registrations/', views.exam_registrations, name='exam_registrations'),
]
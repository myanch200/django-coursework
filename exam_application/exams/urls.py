from django.urls import path
from . import views
app_name = "exams"

urlpatterns = [
  path('exam-registrations/', views.exam_registrations, name='exam_registrations'),
  path('<int:module_id>/create-exam/', views.create_exam, name='create_exam'),
]
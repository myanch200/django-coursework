from django.shortcuts import render

from modules.models import ExamRegistration


def exam_registrations(request):
    exam_registrations = ExamRegistration.objects.all()
    return render(request, 'exams/exam_registrations.html', {'exam_registrations': exam_registrations})
# Create your views here.

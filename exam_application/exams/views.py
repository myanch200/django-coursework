from django.shortcuts import render
from django.contrib.admin.views.decorators import user_passes_test
from modules.models import ExamRegistration

@user_passes_test(lambda u: u.is_superuser)
def exam_registrations(request):
    exam_registrations = ExamRegistration.objects.all()
    return render(request, 'exams/exam_registrations.html', {'exam_registrations': exam_registrations})
# Create your views here.

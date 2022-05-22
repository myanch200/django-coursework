from django.shortcuts import render,redirect
from django.contrib.admin.views.decorators import user_passes_test
from modules.models import ExamRegistration, Module, Exam
from .forms import ExamForm
@user_passes_test(lambda u: u.is_superuser)
def exam_registrations(request):
    exam_registrations = ExamRegistration.objects.all()
    return render(request, 'exams/exam_registrations.html', {'exam_registrations': exam_registrations})


@user_passes_test(lambda u: u.is_superuser)
def create_exam(request,module_id):
    module = Module.objects.get(pk=module_id)
    form = ExamForm()
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.module = module
            exam.save()
            form = ExamForm()
            return render(request, 'partials/_admin_modules_dashboard.html', {'module': module,'form': form})
        else:
          messages.add_message(request, messages.ERROR, 'Невалидни данни!')
          return render('modules/show.html', {'module': module})
    else:
        return redirect('modules:show', module_id=module.id)


@user_passes_test(lambda u: u.is_superuser)
def delete_exam(request,exam_id):
    exam = Exam.objects.get(pk=exam_id)
    form = ExamForm()
    module = exam.module
    exam.delete()
    return render(request, 'partials/_admin_modules_dashboard.html', {'module': module,'form': form})


@user_passes_test(lambda u: u.is_superuser)
def edit_exam(request,exam_id):
    exam = Exam.objects.get(pk=exam_id)
    module = exam.module
    form = ExamForm(instance=exam)
    return render(request, 'partials/_exam_form.html', {'module': module,'form': form})
    
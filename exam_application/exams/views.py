from operator import mod
from django.shortcuts import render,redirect
from django.contrib.admin.views.decorators import user_passes_test
from modules.models import ExamRegistration, Module, Exam
from .forms import ExamForm

# Тук много често използваме декораторът  user_passes_test  който промерява да ли потребителят отговаря на някакво усложие в този случай дали е администратор
# тъй като не искаме обикновен студен да може да вижда, създава и променя информация относно изпити.
@user_passes_test(lambda u: u.is_superuser)
def exam_registrations(request):
    # По този начин с помощта на django orm селектираме вички регистрации за изпит
    #  това грубо преведено към SQL би било SELECT * FROM modules_examregistration
    exam_registrations = ExamRegistration.objects.all() 
    return render(request, 'exams/exam_registrations.html', {'exam_registrations': exam_registrations})

"""
Тук ако потребителят е админ създаваме нов изпит със данниете от POST заявката
"""
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


# Отново проверяваме дали потребителя е админ и ако е взимам изпита чрез параметърът id,който получаваме заедно със заявката
# след това изтриваме, тъй като изолзваме htmx вместо цяла страница накрая връщаме само partial
@user_passes_test(lambda u: u.is_superuser)
def delete_exam(request,exam_id):
    exam = Exam.objects.get(pk=exam_id)
    form = ExamForm()
    module = exam.module
    exam.delete()
    return render(request, 'partials/_admin_modules_dashboard.html', {'module': module,'form': form})

# Ако потребителят е админ визуализираме форма и при ПОСТ заявка ако формата е валидна редактираме изпита
@user_passes_test(lambda u: u.is_superuser)
def edit_exam(request,module_id, exam_id):
    module = Module.objects.get(pk=module_id)
    exam = Exam.objects.get(pk=exam_id)
    form = ExamForm(instance=exam)
    if request.method =='POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            form = ExamForm()
            return render(request, 'modules/show.html', {'module': module,'form': form})
        else:
            messages.add_message(request, messages.ERROR, 'Невалидни данни!')
            return render(request, 'modules/show.html', {'module': module})
    return render(request, 'exams/edit_exam.html', {'module': module,'form': form})
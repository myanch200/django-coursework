from operator import mod
from urllib import request
from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from django.contrib.admin.views.decorators import user_passes_test
from helpers import check_superuser
from django.contrib import messages
from exams.forms import ExamForm
from .forms import ModuleForm
from .models import Module
# Create your views here.
def index(request):
    if request.user.is_superuser:
      modules = Module.objects.all()
    else:
      modules = request.user.modules.all()
    return render(request, 'modules/index.html', {'modules': modules})


def show(request, module_id):
    module = Module.objects.get(pk=module_id)
    form = ExamForm()
    user_is_participant = request.user in module.participants.all()
    context = {
        'module': module,
        'user_is_participant': user_is_participant,
        'form': form
    }
    return render(request, 'modules/show.html', context)


@user_passes_test(lambda u: u.is_superuser)
def new(request):
    form = ModuleForm()
    return render(request, 'modules/new.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def create(request):
    form = ModuleForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Специалността е създадена успешно!')
        return redirect('modules:index')
    else:
        return render(request, 'modules/new.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def edit(request, module_id):
    module = Module.objects.get(pk=module_id)
    form = ModuleForm(instance=module)
    return render(request, 'modules/edit.html', {'form': form, 'module': module})


@user_passes_test(lambda u: u.is_superuser)
def update(request, module_id):
    module = Module.objects.get(pk=module_id)
    form = ModuleForm(request.POST, instance=module)
    if form.is_valid():
        form.save()
        messages.success(request, 'Специалността е обновена успешно!')
        return redirect('modules:index')
    else:
        return render(request, 'modules/edit.html', {'form': form, 'module': module})


@user_passes_test(lambda u: u.is_superuser)
def delete(request, module_id):
    module = Module.objects.get(pk=module_id)
    module.delete()
    messages.success(request, 'Специалността е изтрита успешно!')
    return render(request, 'partials/_modules_list.html', {'modules': Module.objects.all()})



def new_exam_registration(request, module_id, exam_id):
    module = Module.objects.get(pk=module_id)
    exam = module.exams.get(pk=exam_id)
    return render(request, 'modules/new_exam_registration.html', {'module': module, 'exam': exam})


@require_http_methods(['POST'])
def register_for_exam(request, module_id, exam_id):
    module = Module.objects.get(pk=module_id)
    exam = module.exams.get(pk=exam_id)
    
    exam.applications.create(user=request.user, payment_method=request.POST['payment_method'])
    messages.add_message(request, messages.SUCCESS, 'Вие се регистрирахте за изпита.')
    
    return redirect('modules:show', module_id=module_id)
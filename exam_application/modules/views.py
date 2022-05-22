from operator import mod
from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .forms import ModuleForm
from .models import Module
# Create your views here.
def index(request):
    modules = Module.objects.all()
    return render(request, 'modules/index.html', {'modules': modules})

def new(request):
    form = ModuleForm()
    return render(request, 'modules/new.html', {'form': form})

def create(request):
    form = ModuleForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Специалността е създадена успешно!')
        return redirect('modules:index')
    else:
        return render(request, 'modules/new.html', {'form': form})

def edit(request, module_id):
    module = Module.objects.get(pk=module_id)
    form = ModuleForm(instance=module)
    return render(request, 'modules/edit.html', {'form': form, 'module': module})


def update(request, module_id):
    module = Module.objects.get(pk=module_id)
    form = ModuleForm(request.POST, instance=module)
    if form.is_valid():
        form.save()
        messages.success(request, 'Специалността е обновена успешно!')
        return redirect('modules:index')
    else:
        return render(request, 'modules/edit.html', {'form': form, 'module': module})

def show(request, module_id):
    module = Module.objects.get(pk=module_id)
    user_is_participant = request.user in module.participants.all()
    context = {
        'module': module,
        'user_is_participant': user_is_participant,
    }
    return render(request, 'modules/show.html', context)



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
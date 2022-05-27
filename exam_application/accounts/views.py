"""
Тук ни се съдържа фукнциоността за всичко свързано с акаунти като регистрация,
вход виждане на профил, редактиране и отписване от системата
"""
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import ProfileForm, UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

def user_registration(request):
    # ще пренасочим потребители,които вече са се вписали
    if request.user.is_authenticated:
        return redirect('accounts:profile')
    # създаваме нова форма
    form = UserRegistrationForm()
    if request.method == 'POST': # изпълняваме следващите редове само ако заявката е POST
        """
          След това попълваме формата с данните от тази заявка и ако формата е валидна 
          регистрираме новият потребител
        """
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('accounts:profile')
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'accounts/registration.html', context)

def user_login(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')
  
    if request.method == 'POST':
      # отново попълваме формата ако заявката е POST
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Използваме джанго функция, за да впишем потребителя
            user = authenticate(username=username, password=password)
            # Ако потребител с тази паро и потребителско име съществува го вписваме, ако ли не връщаме грешка
            if user is not None:
                login(request, user)
                messages.success(request, f"{username} logged in successfully.")
                return redirect('accounts:profile')
            else:
                messages.error(request, "Wrong credentials , please try again")
    else:
        form = AuthenticationForm()
    # context e просто списък със данни, които да пренесем когато връщаме отговор към потребителя тези данни се използват от нашия 
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

"""
този декоратор ни помага да сме сигурни,че само вписани потребители имат достъп тази 
страница така няма нижда да се притесняваме,че анонимер юзър ще има достъп до някакви данни
тази страница също така си има форма, която ние сме създали във forms.py във същата папка
профил страницата ще ни служи за редактиране на потребителските данни
отново отговаряме на POST заявка, но този път при Get заявка ше визуализираме формата попълнена 
със сегашните данни на вписания юзър

"""
@login_required 
def profile(request):
    form = ProfileForm(request.POST or None, instance=request.user) # instance = request.user взима вписания юзър и попълва формата с неговите данни
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f"Profile updated successfully.")
            return redirect('accounts:profile')
        else:
            messages.add_message(request, messages.ERROR, "Please correct the error below.")
    return render(request, 'accounts/profile.html', {'form': form})

@login_required
def logout_view(request):
    logout(request) # използваме готовата от джанго фукнция, скоято да изтрием потребителя от тази сесия
    return redirect('accounts:login')

from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
def index(request):
    return render(request, 'genshinapp/index.html')

def themes(request):
    if request.method == 'POST':
        form = ThemesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../themes')
    else:
        form = ThemesForm()
    themes = Themes.objects.all()
    data = {
        'themes':themes,
    }
    return render(request, 'genshinapp/themes.html', data)

def reg(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.save()
            return redirect('../main')
    else:
        form = RegForm()
    data = {
        'form':form,
    }
    return render(request, 'genshinapp/reg.html', data)
def themesinside(request, theme_id):
    themes = Themes.objects.filter(id=theme_id)
    data = {
        'themes': themes,
    }
    return render(request,'genshinapp/insidethemes.html', data)

def logout_view(request):
    logout(request)
    return redirect('../main')
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'genshinapp/login.html'
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        return reverse_lazy('main')

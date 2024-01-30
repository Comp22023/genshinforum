from django.shortcuts import render, redirect
from .forms import *

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
    return render(request, 'genshinapp/reg.html')
def themesinside(request, theme_id):
    themes = Themes.objects.filter(id=theme_id)
    data = {
        'themes': themes,
    }
    return render(request,'genshinapp/insidethemes.html', data)

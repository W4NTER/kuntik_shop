from django.shortcuts import render,redirect
from django.views.generic import ListView
from .forms import UserPostForm

from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})


def create(request):
    error = ''

    if request.method == 'POST':
        form = UserPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Вы допустили ошибку при заполнении формы'

    form = UserPostForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/create.html', data)


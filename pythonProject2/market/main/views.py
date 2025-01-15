from django.shortcuts import render,redirect
from select import error

from .forms import Taskform
from .models import Task
from django.views.generic import DetailView





def index(request):

    task = Task.objects.order_by('-id')
    return render(request,'main/index.html', { 'task':task})




def harid(request):
    error = ''
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('harid')
        else:
            error = 'нодуруст'


    form = Taskform()
    context = {
        'form':form,
        'error': error
    }
    return render(request,'main/harid.html',context)


def furush(request):
    return render(request,'main/furush.html')


def test(request):
    return render(request,'main/test.html')
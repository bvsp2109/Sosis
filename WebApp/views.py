from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import *
from .models import *


def Furure_Aim(requrest):
    form=FutureForm(requrest.POST or None)
    if form.is_valid():
        Instance = form.save()
        Instance.save()
        return HttpResponseRedirect('/add/')
    context = {'form': form}
    return render(requrest, 'upload.html', context)

def Details(requrest):
    Data = Future.objects.all()
    return render(requrest,'details.html',{'Data':Data})

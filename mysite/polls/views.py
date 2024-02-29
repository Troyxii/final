from django.shortcuts import render, redirect

from .models import *

from .form import e, eu 

# Create your views here.

def home(request):
    return render(request, 'home.html')


def events(request):
    events = Event.objects.all()
    data = {'events': events}
    return render(request, 'events.html', data)



def admins(request):
    if request.method == 'POST':
        form = eu(request.POST)

        if form .is_valid():
            eve = form.save()
            eve.save()
            return redirect('events')
        
    fo = eu()
    return render(request, 'admin.html', {'fo': fo})

# update eve

def updateeve(request, id):
    news = Event.objects.get(id = id)
    if request.method == 'POST':
        form = e(request.POST, instance=news)

        if form.is_valid():
            reg = form.save()
            return redirect('events')
    else:
        form = e(instance=news)

    return render(request, 'updateve.html', {'id': id, 'form':form})



# Delete register


def deleteve(request, id):
    dele = Event.objects.get(id = id)
    dele.delete()
    return redirect('events')
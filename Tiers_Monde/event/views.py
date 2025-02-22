from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from . models import Events
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    dernier_event = Events.objects.order_by('id')
    context = {'event_list': dernier_event}
    return render(request, 'event/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    return render(request, 'event/detail.html', {'event':event})

def informations(request):
    return render(request, 'event/informations.html')

def my_login(request):
    return render(request, 'event/login.html')

def my_logout(request):
    logout(request)
    return render(request, 'event/logout.html')

def new_password(newpwd):
    newpwd = User.objects.get(username ='new_password')
    newpwd.set_password('new_password')
    newpwd.save()

def register(request):
    return render(request, 'event/register.html')

def registered(request):
    name = request.POST['user_name']
    firstname = request.POST['user_firstname']
    pwd = request.POST['user_pwd']
    email = request.POST['user_email']
    username = firstname[0].lower() + "." + name.lower()    
    user = User.objects.create_user(username, email, pwd)
    user.last_name = name
    user.first_name = firstname
    user.save()
    context = {'user':user}
    return render(request, 'event/registered.html', context)

def welcome(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    context = {'user':user}
    if user is not None :
        login(request, user)
        return render(request, 'event/welcome.html', context)
    else:
        return render(request, 'event/error_log.html')

def contact(request):
    return render(request, 'event/contact.html')

def profil(request):
    return render(request, 'event/resistered/html')
def acheter(request, event_id):
    event = get_object_or_404(Events, pk=event_id)
    event.av_ticket -= 1
    event.save()
    return render(request, 'event/acheter.html', {'event':event})

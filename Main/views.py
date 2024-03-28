from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Calendar, Event, UserCalendar
from .forms import CalendarForm, EventForm
from datetime import datetime, timedelta, date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser


# Create your views here.

def home(request):
    if request.user.is_authenticated: 
       user_calendars = UserCalendar.objects.filter(user=request.user)
       events = Event.objects.filter(calendar__in=user_calendars.values('calendar'))
       user_created_calendars = Calendar.objects.filter(users=request.user)
       context = {'user_calendars':user_calendars, 'events':events, 'user_created_calendars':user_created_calendars}
       return render(request, 'Main/home.html',context)
    else:
        return render(request,'Main/home.html',{'not_authenticated':True})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = User.objects.create_user(username=username, password=password, email=email)
            return redirect ('login')
        else:
            messages.error(request,"Passwords dont match")
    
    return render(request, 'Main/SignUp.html')

def loginPage(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('home')
        else:
            messages.error(request, "Username or password does not exist")
            
    context = {}
    return render(request, 'Main/SignIn.html' , context)

def logoutUser(request):
    logout(request)
    return redirect ('home')

def MyCalendar(request):
    return render(request, 'Main/MyCalendar.html')

def CreateCalender(request):
    if request.method == 'POST':
        form = CalendarForm(request.POST) 
        if form.is_valid():
            calendar = form.save()
            UserCalendar.objects.create(user=request.user , calendar= calendar)
            return redirect ('home')
    
    else:
        form = CalendarForm()
        context = {'form':form}
    return render(request,'Main/CreateCalendar.html', context)


def CreateEvent(request,calendar_id):
    calendar = Calendar.objects.get(id=calendar_id)
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.date_and_time = datetime.combine(form.cleaned_data['date'], form.cleaned_data['time'])
            event.calendar = calendar
            event.save()
            return redirect ('calendar_detail', calendar_id=calendar.id)
    else:
        form = EventForm()
        context= {'form':form, 'calendar':calendar}
        return render(request,'Main/CreateEvent.html',context)

def calendar_detail(request,calendar_id):
    today = date.today()
    if today.weekday() == 0:
        start_of_week = today
    else:
        start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    calendar = Calendar.objects.get(id=calendar_id)
    events = Event.objects.filter(calendar=calendar)
    days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

    offset_weeks = int(request.GET.get('offset', 0))  # Get offset from query string
    if offset_weeks != 0:
        start_of_week += timedelta(days=offset_weeks * 7)
        end_of_week = start_of_week + timedelta(days=6)
    
    time_slots = ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00']
    context = {
        'calendar':calendar,
        'events':events,
        'days':days,
        'time_slots':time_slots,
        'start_of_week':start_of_week,
        'end_of_week':end_of_week,
        }

    return render(request,'Main/calender_detail.html',context)

def delete_calendar(request, calendar_id):
    calendar = Calendar.objects.get(id=calendar_id)
    calendar.delete()
    return redirect('home')

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    calendar_id = event.calendar.id
    event.delete()
    return redirect('calendar_detail', calendar_id=calendar_id)

def edit_calendar(request, calendar_id):
    calendar = get_object_or_404(Calendar, id=calendar_id)

    if request.method == 'POST':
        form = CalendarForm(request.POST, instance=calendar)
        if form.is_valid():
            form.save()
            return redirect('calendar_detail',calendar_id = calendar_id)
    else:
        form = CalendarForm(instance=calendar)
    return render(request, 'Main/edit_calendar.html',{'form':form,'calendar':calendar})

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('calendar_detail',calendar_id = event.calendar.id)
    else:
        form = EventForm(instance=event)
    return render(request, 'Main/edit_event.html',{'form':form,'event':event})

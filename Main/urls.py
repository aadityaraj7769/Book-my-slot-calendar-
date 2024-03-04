from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home' ),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('mycalendar/', views.MyCalendar, name='MyCalendar'),
    path('createcalender/',views.CreateCalender, name='CreateCalendar'),
    path('create_event/<int:calendar_id>/',views.CreateEvent, name='CreateEvent'),
    path('calendar_detail/<int:calendar_id>/', views.calendar_detail, name='calendar_detail'),
]
from django import forms
from .models import Calendar, Event

class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ['name','description']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title','date','time']

    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))

    
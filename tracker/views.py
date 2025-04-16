from django.shortcuts import render, redirect
from .models import Event

def home(request):
    if request.method == "POST":
        date = request.POST['date']
        note = request.POST['note']
        Event.objects.create(date=date, note=note)
        return redirect('home')
    
    events = Event.objects.all().order_by('date')
    return render(request, 'tracker/home.html', {'events': events})

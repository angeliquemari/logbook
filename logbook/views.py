from django.shortcuts import render, get_object_or_404, redirect
from .models import Dive, Diver

def dive_list(request):
    dives = Dive.objects.all().order_by('-date', '-start_time')
    return render(request, 'logbook/dive_list.html', {'dives': dives})

def dive_detail(request, pk):
    dive = get_object_or_404(Dive, pk=pk)
    dive_duration = dive.duration*60
    return render(request, 'logbook/dive_detail.html', {'dive': dive, 'dive_duration': dive_duration})

def profile(request):
    diver = get_object_or_404(Diver, account=request.user)
    date_of_last_dive = diver.get_date_of_last_dive()
    total_number_of_dives = diver.get_total_number_of_dives()
    return render(request, 'logbook/profile.html', {'diver': diver, 'date_of_last_dive': date_of_last_dive, 'total_number_of_dives': total_number_of_dives})

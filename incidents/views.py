from django.shortcuts import render,redirect, get_object_or_404
from .models import incidents_detail
from .forms import IncidentForm
from django.contrib import messages

def report_incidents(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your incident has been reported.')
            return redirect('incident_dashboard')  # Redirect to a success page or incident list
        else:
            messages.success(request, 'Your incident not been reported.')
    form = IncidentForm()
    return render(request, 'report_incident.html', {'form': form})

def incident_list(request):
    incidents = incidents_detail.objects.all()
    return render(request, 'incident_list.html', {'incidents': incidents})

def incident_dashboard(request):
    incidents = incidents_detail.objects.all()
    return render(request, 'incident_dashboard.html', {'incidents': incidents})

def incident_detail(request, incident_id):
    incident = get_object_or_404(incidents_detail, pk=incident_id)
    return render(request, 'incident_detail.html', {'incident': incident})



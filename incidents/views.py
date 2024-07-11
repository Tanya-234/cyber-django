from django.shortcuts import render,redirect, get_object_or_404
from .models import incidents_detail
from .forms import IncidentForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

def report_incidents(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Your incident has been reported.')
            return redirect('incident_dashboard')  # Redirect to a success page or incident list
        else:
            messages.error(request, 'Your incident not been reported.')
    else:
         form = IncidentForm()
    return render(request, 'report_incident.html', {'form': form})

def incident_list(request):
    incidents = incidents_detail.objects.all()
    return render(request, 'incident_list.html', {'incidents': incidents})



def incident_dashboard(request):
    query = request.GET.get('q')
    severity = request.GET.get('severity')
    status = request.GET.get('status')
    
    # Start with all incidents
    incidents = incidents_detail.objects.all()
    
    if query:
        # Apply a filter based on the 'query' parameter
        incidents = incidents.filter(
            Q(type__icontains=query) | Q(severity__icontains=query) | Q(status__icontains=query)
        )
    
    if severity:
        # Apply a filter based on the 'severity' parameter
        incidents = incidents.filter(severity=severity)
    
    if status:
        # Apply a filter based on the 'status' parameter
        incidents = incidents.filter(status=status)
    
    # Configure pagination
    paginator = Paginator(incidents, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Calculate starting serial number
    starting_serial_number = (page_obj.number - 1) * paginator.per_page + 1
    if page_obj.number > 1:
        previous_page_last_serial = (page_obj.number - 2) * paginator.per_page + paginator.per_page
        starting_serial_number = previous_page_last_serial + 1
    
    context = {
        'page_obj': page_obj,
        'starting_serial_number': starting_serial_number,
    }
    
    return render(request, 'incident_dashboard.html', context)



def incident_detail(request, incident_id):
    incident = get_object_or_404(incidents_detail, pk=incident_id)
    return render(request, 'incident_detail.html', {'incident': incident})


def delete_incident(request, incident_id):
    incident = get_object_or_404(incidents_detail, pk=incident_id)
    if request.method == 'POST':
        incident.delete()
        messages.success(request, 'Incident deleted successfully.')
        return redirect('incident_dashboard')
    return render(request, 'delete_incident.html', {'incident': incident})



    
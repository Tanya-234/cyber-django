from django import forms
from .models import incidents_detail
    
class IncidentForm(forms.ModelForm):
    class Meta:
        model = incidents_detail
        fields = ['type', 'description','severity', 'Report_date', 'status','evidence']
    
    
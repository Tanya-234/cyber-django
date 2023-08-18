from django.urls import path
from .views import report_incidents,incident_list,incident_dashboard,incident_detail
                    
urlpatterns = [
    path('report/', report_incidents, name='report_incident'),
    path('list/', incident_list, name='incident_list'), 
    path('dashboard/', incident_dashboard, name='incident_dashboard'),
    path('incident/<int:incident_id>/', incident_detail, name='incident_detail'),                 
    ]
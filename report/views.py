from django.shortcuts import render
from .models import Incident


def report_list(request):
    incidents = Incident.objects.order_by('-date_time')
    return render(request, 'report/report_list.html', {'incidents': incidents})

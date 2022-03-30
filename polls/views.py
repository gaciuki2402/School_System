from multiprocessing import context
from django.shortcuts import render
from .models import Dashboard

def index(request):
    latest_dashboard=Dashboard.objects.all()
    context={
        'latest_dashboard':latest_dashboard,
    }
    return render(request, 'polls/indexes.html', context)


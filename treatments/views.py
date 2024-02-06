from django.shortcuts import render
from .models import Massage

# Create your views here.


def home(request):
    massages = Massage.objects.all()
    return render(request, 'treatments/home.html', {'massages': massages})

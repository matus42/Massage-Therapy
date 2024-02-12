from django.shortcuts import render
from .models import Massage
from django.views.generic import DetailView

# Create your views here.


def home(request):
    massages = Massage.objects.all()
    return render(request, 'treatments/home.html', {'massages': massages})


class MassageDetailView(DetailView):
    model = Massage
    template_name = 'treatments/massage_detail.html'
    context_object_name = 'massage'

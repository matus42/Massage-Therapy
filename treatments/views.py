from django.shortcuts import render
from .models import Massage
from django.views.generic import DetailView


def home(request):
    """
    Render the homepage with a list of massages.
    """
    massages = Massage.objects.all()
    return render(request, 'treatments/home.html', {'massages': massages})


class MassageDetailView(DetailView):
    """
    Display detailed information for a specific massage.
    """
    model = Massage
    template_name = 'treatments/massage_detail.html'
    context_object_name = 'massage'

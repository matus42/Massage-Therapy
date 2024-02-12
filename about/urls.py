from django.urls import path
from .views import about_page

urlpatterns = [
    path('about/', about_page, name='about'),
]

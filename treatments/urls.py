from django.urls import path
from .views import home, MassageDetailView

urlpatterns = [
    path('', home, name='home'),
    path('massages/<int:pk>/',
         MassageDetailView.as_view(),
         name='massage_detail'),
]

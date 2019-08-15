from django.urls import path,include
from django.views.generic import ListView, DetailView
from services.models import Servicesss

urlpatterns = [
    path('', ListView.as_view(queryset=Servicesss.objects.all(),template_name="services/usl.html"),name="services"),
]
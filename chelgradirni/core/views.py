from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from core.models import Cooler

class CoolerListView(ListView):
    model = Cooler
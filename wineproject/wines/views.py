from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Wine

class WineListView(ListView):
    model = Wine
    template_name = "wines/list.html"
    context_object_name = "wines"

class WineDetailView(DetailView):
    model = Wine
    template_name = "wines/_detail.html"
    context_object_name = "wine"

class WineCreateView(CreateView):
    model = Wine
    fields = ["name", "year", "region", "grape", "notes"]
    template_name = "wines/_form.html"
    success_url = reverse_lazy("wine_list")

class WineUpdateView(UpdateView):
    model = Wine
    fields = ["name", "year", "region", "grape", "notes"]
    template_name = "wines/_form.html"
    success_url = reverse_lazy("wine_list")

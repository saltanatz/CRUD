from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Country

def main_page(request):
    return render(request, 'main_page.html')

class CountryListView(ListView):
    model = Country
    template_name = 'country_list.html'
    context_object_name = 'countries' 

class CountryCreateView(CreateView):
    model = Country
    fields = ['cname', 'population']
    template_name = 'country_form.html'
    success_url = reverse_lazy('country_list')

class CountryUpdateView(UpdateView):
    model = Country
    fields = ['cname', 'population']
    template_name = 'country_form.html'
    success_url = reverse_lazy('country_list')

class CountryDeleteView(DeleteView):
    model = Country
    template_name = 'country_confirm_delete.html'
    success_url = reverse_lazy('country_list')

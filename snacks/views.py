from django.shortcuts import render
from .models import Snack
from django.views.generic import ( ListView,
                                   CreateView,
                                   UpdateView,
                                   DeleteView,
                                   DetailView,
                                   
                                    )





class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack

class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack


class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ["name", "purchaser", "description"]



class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ["name", "description"]

class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url ='/'



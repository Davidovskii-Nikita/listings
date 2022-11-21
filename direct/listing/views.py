from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from .models import Listing


class ListingView(ListView):
    model = Listing
    template_name = 'listing/listing.html'
    context_object_name = 'listings'
    slug_url_kwarg = 'lising_slug'

    def get_queryset(self, **kwargs):
        return Listing.objects.filter(is_published = True)
# Create your views here.

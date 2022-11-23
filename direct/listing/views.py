from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.timezone import now
from django.views.generic import TemplateView, DetailView, ListView

from .forms import ReviewForm
from .models import Listing, Review



class ListingView(ListView):
    model = Listing
    template_name = 'listing/listing.html'
    context_object_name = 'listings'

    def get_queryset(self, **kwargs):
        return Listing.objects.filter(is_published = True)

class ListingDetailView(DetailView):
    model = Listing
    template_name = 'listing/listing-details.html'
    slug_url_kwarg = 'listing_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listing']= Listing.objects.filter(slug=self.kwargs['listing_slug'])[0]
        context['reviews'] = Review.objects.filter(Q(listing = self.object) and Q(is_published = True))
        context['form'] = ReviewForm
        return context

    def post(self, request: HttpRequest,  *args, **kwargs):
        form = ReviewForm(data =request.POST)

        for field in form:
            print("Field Error:", field.name, field.errors)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.date_published = now()
            post.is_published = True
            post.listing = Listing.objects.get(slug = self.kwargs['listing_slug'])

            form.save()

        return self.get(request=request)

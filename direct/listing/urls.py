from django.urls import path

from .views import ListingView, ListingDetailView

urlpatterns = [
    path('',ListingView.as_view(), name= 'listing'),
    path('<slug:listing_slug>',ListingDetailView.as_view(), name= 'listing_det')
]
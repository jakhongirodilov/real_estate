from django.forms import modelformset_factory
from django.template import RequestContext
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ListingForm, ListingFilterForm, ImageForm
from .models import Listing, Booking, ListingImage


def index(request):
    listings = Listing.objects.filter(is_active=True).order_by('-created_at')
    filter_form = ListingFilterForm(request.GET)

    if filter_form.is_valid():
        # Extract filter parameters from the form
        num_rooms = filter_form.cleaned_data.get('num_rooms')
        city = filter_form.cleaned_data.get('city')
        region = filter_form.cleaned_data.get('region')
        property_type = filter_form.cleaned_data.get('property_type')
        listing_type = filter_form.cleaned_data.get('listing_type')

        # Apply filters to the queryset
        if num_rooms:
            listings = listings.filter(num_rooms=num_rooms)
        if city:
            listings = listings.filter(city__icontains=city)
        if region:
            listings = listings.filter(region__icontains=region)
        if property_type:
            listings = listings.filter(property_type=property_type)
        if listing_type:
            listings = listings.filter(listing_type=listing_type)

    context = {
        'listings': listings,
        'filter_form': filter_form,
    }

    return render(request, 'index.html', context)

@login_required(login_url='login')
def create_listing(request):
    ImageFormSet = modelformset_factory(ListingImage, form=ImageForm, extra=3)

    if request.method == 'POST':
        form = ListingForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=ListingImage.objects.none())

        if form.is_valid() and formset.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()

            for form in formset.cleaned_data:
                image = form['image']
                photo = ListingImage(listing=listing, image=image)
                photo.save()

            messages.success(request, "Posted!")

            return redirect('home')
    else:
        form = ListingForm()
        formset = ImageFormSet(queryset=ListingImage.objects.none())

    context = {
        'form': form,
        'formset':formset
    }

    # return render(request, 'new_listing.html', context, context_instance=RequestContext(request))
    return render(request, 'new_listing.html',{'form': form, 'formset': formset})


@login_required(login_url='login')
def listing(request, id):
    listing = get_object_or_404(Listing, id=id)
    photos = ListingImage.objects.filter(listing = listing)
    current_user = request.user
    booked_listing = None

    booked_listings = Booking.objects.filter(user=current_user)
    for booking in booked_listings:
        if booking.listing == listing:
            booked_listing = Booking.objects.get(listing=listing)

    context = {
        'listing': listing,
        'booked_listing':booked_listing,
        'current_user':current_user,
        'photos':photos
    }

    return render(request, 'listing.html', context)

@login_required(login_url='login')
def my_listings(request):
    current_user = request.user
    listings = Listing.objects.filter(owner = current_user)

    context = {
        "listings": listings
    }

    return render(request, 'my_listings.html', context)

def toggle_listing(request, id):
    listing = get_object_or_404(Listing, id=id, owner=request.user)

    if listing.is_active:
        listing.is_active = False
    elif not listing.is_active and not listing.booked:
        listing.is_active = True
    listing.save()

    return redirect('my_listings')

@login_required(login_url='login')
def delete_listing(request, id):
    listing = get_object_or_404(Listing, id=id, owner=request.user)
    listing.delete()
    return redirect('my_listings')

@login_required(login_url='login')
def book_listing(request, listing_id):
    if request.method == 'POST':
        listing = get_object_or_404(Listing, pk=listing_id)
        user = request.user

        # Check if the user has sufficient balance
        booking_cost = listing.booking_cost
        if user.balance >= booking_cost and listing.owner != user:  # Specify the amount needed for booking
            # Process the booking
            Booking.objects.create(user=user, listing=listing, amount_paid=booking_cost)
            user.balance -= booking_cost
            user.save()

            listing.owner.balance += booking_cost
            listing.owner.save()

            # Set the listing as inactive
            listing.is_active = False
            listing.booked = True
            listing.save()

            messages.success(request, 'Listing booked successfully.')
        else:
            messages.error(request, 'Insufficient balance to book the listing.')

        return redirect('my_bookings')

@login_required(login_url='login')
def cancel_booking(request, booking_id):
    if request.method == 'POST':
        booking = Booking.objects.get(pk=booking_id)

        returned_money = booking.amount_paid * 0.7

        # Refund the user and deduct from the owner's balance
        booking.user.balance += returned_money
        booking.user.save()

        booking.listing.owner.balance -= returned_money
        booking.listing.owner.save()


        booking.listing.is_active = True
        booking.listing.booked = False
        booking.listing.save()

        booking.delete()

        messages.success(request, 'Booking cancelled. Amount refunded.')

        return redirect('my_bookings')

@login_required(login_url='login')
def my_bookings(request):
    user = request.user
    booked_listings = Booking.objects.filter(user=user)

    context = {
        'booked_listings': booked_listings
    }

    return render(request, 'bookings.html', context)


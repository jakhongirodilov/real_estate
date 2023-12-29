from django.urls import path
from .views import index, create_listing, listing, my_listings, toggle_listing, delete_listing, my_bookings, book_listing, cancel_booking


urlpatterns = [
    path("", index, name="home"),
    path("new_listing/", create_listing, name="new_listing"),
    path("listing/<int:id>/", listing, name="listing"),
    path("my_listings/", my_listings, name="my_listings"),
    path('toggle_listing/<int:id>/', toggle_listing, name='toggle_listing'),
    path('delete_listing/<int:id>/', delete_listing, name='delete_listing'),
    path('my_bookings/', my_bookings, name="my_bookings"),
    path('book_listing/<int:listing_id>/', book_listing, name='book_listing'),
    path('cancel_booking/<int:booking_id>/', cancel_booking, name='cancel_booking'),
]
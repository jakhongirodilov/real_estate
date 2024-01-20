from django.test import TestCase
from .models import CustomUser, Listing, ListingType, PropertyType, ListingImage, Booking


class ListingTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='test_user')
        self.property_type = PropertyType.objects.create(property_type='Apartment')
        self.listing_type = ListingType.objects.create(listing_type='For Sale')
        self.listing = Listing.objects.create(
            owner=self.user,
            num_rooms=2,
            num_bedroom=1,
            num_bathrooms=1,
            size=100.5,
            address='123 Main St',
            city='Test City',
            region='Test Region',
            cost=100000,
            property_type=self.property_type,
            listing_type=self.listing_type,
            is_active=True,
            booked=False,
            booking_cost=200,
        )

    def test_listing_str(self):
        self.assertEqual(
            str(self.listing),
            '2 room Apartment in Test City'
        )

class ListingTypeTestCase(TestCase):
    def test_listing_type_str(self):
        listing_type = ListingType.objects.create(listing_type='For Rent')
        self.assertEqual(str(listing_type), 'For Rent')

class PropertyTypeTestCase(TestCase):
    def test_property_type_str(self):
        property_type = PropertyType.objects.create(property_type='House')
        self.assertEqual(str(property_type), 'House')

class ListingImageTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='test_user')
        self.property_type = PropertyType.objects.create(property_type='Apartment')
        self.listing_type = ListingType.objects.create(listing_type='For Sale')
        self.listing = Listing.objects.create(
            owner=self.user,
            num_rooms=2,
            num_bedroom=1,
            num_bathrooms=1,
            size=100.5,
            address='123 Main St',
            city='Test City',
            region='Test Region',
            cost=100000,
            property_type=self.property_type,
            listing_type=self.listing_type,
            is_active=True,
            booked=False,
            booking_cost=200,
        )
        self.listing_image = ListingImage.objects.create(
            listing=self.listing,
            image='test_image.jpg'
        )

    def test_listing_image_str(self):
        self.assertEqual(
            str(self.listing_image),
            f'Image for {self.listing}'
        )

class BookingTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='test_user')
        self.property_type = PropertyType.objects.create(property_type='Apartment')
        self.listing_type = ListingType.objects.create(listing_type='For Sale')
        self.listing = Listing.objects.create(
            owner=self.user,
            num_rooms=2,
            num_bedroom=1,
            num_bathrooms=1,
            size=100.5,
            address='123 Main St',
            city='Test City',
            region='Test Region',
            cost=100000,
            property_type=self.property_type,
            listing_type=self.listing_type,
            is_active=True,
            booked=False,
            booking_cost=200,
        )
        self.booking = Booking.objects.create(
            user=self.user,
            listing=self.listing,
            amount_paid=150.75,
        )

    def test_booking_str(self):
        self.assertEqual(
            str(self.booking),
            f'test_user booked {self.listing}'
        )
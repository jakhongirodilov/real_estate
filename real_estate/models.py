from django.db import models
from users.models import CustomUser


class Listing(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    num_rooms = models.IntegerField()
    num_bedroom = models.IntegerField()
    num_bathrooms = models.IntegerField()
    size = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=70)
    region = models.CharField(max_length=70)
    cost = models.IntegerField()

    property_type = models.ForeignKey('PropertyType', on_delete=models.SET_DEFAULT, default=None)
    listing_type = models.ForeignKey('ListingType', on_delete=models.SET_DEFAULT, default=None)

    is_active = models.BooleanField(default=True)
    booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    booking_cost = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.num_rooms} room {self.property_type} in {self.city}"

class ListingType(models.Model):
    listing_type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.listing_type

class PropertyType(models.Model):
    property_type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.property_type


def get_image_filename(instance, filename):
    id = instance.listing.id
    return "post_images/%s" % (id)

class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, default=None, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to=get_image_filename, verbose_name='Image')

    def __str__(self):
        return f"Image for {self.listing}"

class Booking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="booking")
    amount_paid = models.FloatField()

    def __str__(self):
        return f"{self.user.username} booked {self.listing}"



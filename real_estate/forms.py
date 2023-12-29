from django import forms
from django.forms import ClearableFileInput
from .models import Listing, PropertyType, ListingType, ListingImage

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        exclude = ['owner']


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = ListingImage
        fields = ('image', )

class ListingFilterForm(forms.Form):
    num_rooms = forms.IntegerField(required=False)
    city = forms.CharField(max_length=70, required=False)
    region = forms.CharField(max_length=70, required=False)
    property_type = forms.ModelChoiceField(queryset=PropertyType.objects.all(), required=False)
    listing_type = forms.ModelChoiceField(queryset=ListingType.objects.all(), required=False)





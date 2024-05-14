from rest_framework import serializers
from .models import Listing, ListingAmenity, ListingImage, ListingReview


class ListingAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingAmenity
        fields = '__all__'


class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = '__all__'


class ListingReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingReview
        fields = '__all__'



class ListingSerializer(serializers.ModelSerializer):
    amenities = ListingAmenitySerializer(many=True)
    images = ListingImageSerializer(many=True)
    reviews = ListingReviewSerializer(many=True)

    class Meta:
        model = Listing
        fields = ['id', 'title', 'date', 'description', 'location', 'price', 'host', 'amenities', 'images', 'reviews']
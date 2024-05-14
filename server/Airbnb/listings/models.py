from django.db import models
from users.models import Host

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    host = models.ForeignKey(Host, on_delete=models.CASCADE)


class ListingAmenity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)


class ListingImage(models.Model):
    image = models.ImageField(upload_to='listing_images/')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)


class ListingReview(models.Model):
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
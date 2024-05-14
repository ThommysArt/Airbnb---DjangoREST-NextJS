from django.db import models
from users.models import User
from listings.models import Listing

# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    date = models.DateField()
    method = models.CharField(max_length=100)


class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
from django.db import models

# Create your models here.
class Meds(models.Model):
    class MedsPrescription(models.TextChoices):
        yes = "Yes"
        no = "No"

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    prescription = models.CharField(
        max_length = 3,
        choices = MedsPrescription.choices,
        default = MedsPrescription.yes,
    )


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    medName = models.CharField(max_length=30)
    quantity = models.IntegerField()
    dateOrdered = models.CharField(max_length=30)
    price = models.IntegerField(default=100)
    delivered = models.BooleanField()

class Transaction(models.Model):
    id = models.IntegerField(primary_key=True)
    key = models.IntegerField()
    status = models.CharField(max_length=30)
    dateOrdered = models.CharField(max_length=30)
    expectedDeliveryDate = models.CharField(max_length=30)
    currentStatus = models.CharField(max_length=30)

class CartNumber(models.Model):
    cartItemsNumber = models.IntegerField()
    id = models.IntegerField(primary_key=True)


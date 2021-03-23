from django.db import models

class Lot(models.Model):
    total_spaces = models.IntegerField(default=0)
    available_spaces = models.IntegerField(default=0)
    available_spaces_lrg = models.IntegerField(default=0)
    reserved_spaces = models.IntegerField(default=0)
    location = models.CharField(default='', max_length=10000)
    nickname = models.CharField(default='', max_length=10000)

class Reservation(models.Model):
    lot = models.ForeignKey("Lot", on_delete=models.CASCADE)
    date = models.DateField()
    license_plate = models.CharField(default=0, max_length=8)


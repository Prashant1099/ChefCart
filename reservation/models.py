from django.db import models


class Reservation(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField()
    noOfPeople = models.IntegerField()
    phoneNo = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()

    class Meta:
        verbose_name = 'reservation'
        verbose_name_plural = 'reservations'

    def __str__(self):
        return self.firstName + ' ' + self.lastName
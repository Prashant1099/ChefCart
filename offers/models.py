from django.db import models

class Offers(models.Model):
    mealName = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='Offers/')
    price = models.IntegerField()


    class Meta:
        verbose_name = 'offer'
        verbose_name_plural = 'offers'

    def __str__(self):
        return self.mealName



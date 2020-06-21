from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    phoneNo = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'contact us'

    def __str__(self):
        return self.name

    

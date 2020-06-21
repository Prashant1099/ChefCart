from django.db import models

class About(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='About/')

    class Meta:
       verbose_name_plural = 'about'

    def __str__(self):
        return self.title

class WhyChooseUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'why choose us'

    def __str__(self):
        return self.title   

class Chefs(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    image = models.ImageField(upload_to='Chefs/')

    class Meta:
        verbose_name = 'chef'
        verbose_name_plural = 'chefs'

    def __str__(self):
        return self.name
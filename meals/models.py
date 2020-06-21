from django.db import models
from django.utils.text import slugify

class Meals(models.Model):
    mealName = models.CharField(max_length=25)
    description = models.CharField(max_length=500)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    noOfPeople = models.IntegerField()
    price = models.IntegerField(null=True, blank=True)
    prepTime = models.IntegerField()
    image = models.ImageField(upload_to='Meals/')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.mealName:
            self.slug = slugify(self.mealName)
        super(Meals, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'meal'
        verbose_name_plural = 'meals'

    def __str__(self):
        return self.mealName

class Category(models.Model):
    category = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category
from django.db import models
from django.urls import reverse

# Create your models here.
class Animal(models.Model):
    name=models.CharField(max_length=35,db_index=True)
    gender=models.CharField(max_length=6,)
    age=models.DecimalField(decimal_places=1,max_digits=10)
    appearence=models.TextField(blank=True,)
    description=models.TextField(blank=True,verbose_name='Character',default='A very nice pet!')
    photo=models.ImageField(upload_to='photo/', blank=True)
    available=models.BooleanField(default=False,verbose_name='In home searching')
    curator=models.ForeignKey("Curator",on_delete=models.PROTECT,null=True)
    category=models.ForeignKey('Category',on_delete=models.PROTECT,null=False,verbose_name='Category')

    def get_absolute_url(self):
        return reverse('view_animals', kwargs={"animal_id": self.pk})




class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category', db_index=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
            return reverse('view_category', kwargs={"category_id": self.pk})


class Curator(models.Model):
    name = models.CharField(max_length=100, verbose_name='Curator', db_index=True)
    photo = models.ImageField(upload_to='photo/', blank='True')
    organization = models.CharField(max_length=50, )
    addres=models.TextField()
    description=models.TextField(blank=True,verbose_name="About curator")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view_curators', kwargs={"curator_id": self.pk})


from django.db import models
from django.urls import reverse


class Animal(models.Model):
    gender=[('M','Male'),('F','Female'),]
    name=models.CharField(max_length=35,db_index=True)
    gender=models.CharField(max_length=6,choices=gender,blank=False)
    age=models.DecimalField(decimal_places=1,max_digits=10)
    appearence=models.TextField(blank=True,)
    description=models.TextField(blank=True,verbose_name='Character',default='A very nice pet!')
    photo=models.ImageField(upload_to='photo/', blank=True)
    available=models.BooleanField(default=True,verbose_name='In home searching')
    curator=models.ForeignKey("Curator",on_delete=models.PROTECT,null=True)
    category=models.ForeignKey('Category',on_delete=models.PROTECT,null=False,verbose_name='Category')

    def get_absolute_url(self):
        return reverse('view_animals', kwargs={"animal_id": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category', db_index=True)
    photo = models.ImageField(upload_to='photo/category', blank=True)
    back_photo= models.ImageField(upload_to='photo/bphoto', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
            return reverse('category', kwargs={"category_id": self.pk})


class Curator(models.Model):
    name = models.CharField(max_length=100, verbose_name='Curator', db_index=True)
    photo = models.ImageField(upload_to='photo/', blank='True')
    organization = models.CharField(max_length=50, )
    addres=models.TextField()
    description=models.TextField(blank=True,verbose_name="About curator")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('curator_details', kwargs={"curator_id": self.pk})

class News(models.Model):
    title=models.CharField(max_length=140)
    photo=models.ImageField(upload_to='photo/', blank='True')
    description=models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('news', kwargs={"news_id": self.pk})

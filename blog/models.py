from django.db import models
from django.urls import reverse


# Create your models here.
class Sale(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='index/img')

    def __str__(self):
        return self.name

class Add(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='index/img')
    price = models.IntegerField()
    bio = models.TextField()


    def __str__(self):
        return self.name


class Lap(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='index/img')
    slug = models.SlugField(max_length=300)
    price = models.IntegerField()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("laptopsDetail", args=[self.slug])



class Laptop(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='index/img')
    slug = models.SlugField(max_length=300)
    price = models.IntegerField()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("laptopsDetail", args=[self.slug])


class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    number = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name














































































































































































from django.db import models
from django.contrib.auth.models import User


# Create your models here.





    
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)
    description=models.TextField()

    def __str__(self):
        return f'message from {self.name}'
    
class Blogs(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    authname=models.CharField(max_length=30)
    img=models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    timestamp=models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return f'messagefrom {self.authname}'
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Blogs'
        verbose_name_plural = 'Blogs'


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description

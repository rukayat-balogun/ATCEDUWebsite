from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)


class Category(models.Model):
    title = models.CharField(max_length=250)
    slug  = models.SlugField(unique=True)

    class Meta: 
        verbose_name_plural = "categories"
        
    def get_absolute_url(self):
        return self.slug
    
    


class Item(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta: 
        verbose_name_plural = "items"

    def __str__(self):
        self.name 
    
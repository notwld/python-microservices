from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    likes = models.PositiveIntegerField()
    img = models.CharField(max_length=300)

    def __str__(self) -> str:
        return str(self.title)
    
class User(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.name) 
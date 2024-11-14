from django.db import models

# Create your models here.

class Customer(models.Model):
    email = models.EmailField()
    password = models.TextField()


    def __str__(self):
        return self.email
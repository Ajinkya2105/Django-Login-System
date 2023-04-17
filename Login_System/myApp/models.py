from django.db import models

# Create your models here.
class Customer(models.Model):
    Email = models.EmailField(max_length=254)
    pass1 = models.CharField(max_length=50)
    pass2 = models.CharField(max_length=50)

    def __str__(self):
        return self.Email
    

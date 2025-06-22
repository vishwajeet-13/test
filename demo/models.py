from django.db import models

# Create your models here.
class Demo(models.Model):
    test_data = models.CharField(max_length=254)
from django.db import models

# Create your models here.
# models is a python file that contains the classes that represent the database tables
class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    
    #as the name appeared in the table item
    def __str__(self):
        return self.name
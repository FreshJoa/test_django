from distutils.command import upload

from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length = 128)
    description = models.TextField(default= "")
    year = models.IntegerField(null = True, blank= True)
    released = models.DateField( null = True, blank= True)
    rating = models.DecimalField( null = True, blank= True, decimal_places= 2, max_digits= 10)
    photo = models.ImageField( null = True, blank= True, upload_to= 'plakaty')

    def __str__(self):
        return self.name_with_year()

    def name_with_year(self):
        return str(self.name)+ " (" + str(self.year)+")"



# Create your models here.

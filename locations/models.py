from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    iso2 = models.CharField(max_length=2, unique=True)
    iso3 = models.CharField(max_length=3,unique=True)
    iso_numeric = models.CharField(max_length=3, unique=True)

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')
    iso2 = models.CharField(max_length=2, null=True, blank=True)
    iso3 = models.CharField(max_length=3, null=True, blank=True)  
    iso_numeric = models.CharField(max_length=3, null=True, blank=True)

    class Meta:
        unique_together = [ 
            ('country', 'iso2', 'iso3', 'iso_numeric')
        ]
    def __str__(self):
        return f"{self.name}"

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return f"{self.name}"
    
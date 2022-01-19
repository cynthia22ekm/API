from django.db import models

class employees(models.Model):
   firstname=models.CharField(max_length=10)
   lastname=models.CharField(max_length=10)
   id=models.IntegerField(primary_key=True)
   Gender=models.CharField(max_length=10)
   Nationality=models.CharField(max_length=10)

   def __str__(self):
       return self.firstname

class nationality(models.Model):
   countrycode=models.CharField(max_length=10)
   countrydesc=models.CharField(max_length=10)
   id=models.IntegerField

   def __str__(self):
       return self.countrycode

class residence(models.Model):
   residencecode=models.CharField(max_length=10)
   residencedesc=models.CharField(max_length=10)

   def __str__(self):
       return self.residencecodeode

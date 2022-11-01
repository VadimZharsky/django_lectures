from email.policy import default
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(120)])
    heartrate = models.IntegerField(default=60, validators=[MinValueValidator(1),MaxValueValidator(300)])

    def __str__(self):
        return f"{self.last_name},{self.first_name} is {self.age} years old"
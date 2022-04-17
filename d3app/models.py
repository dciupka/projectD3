from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

class Name(Model):
    name = models.CharField(max_length=10)
    age = IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])

    def __str__(self):
        return self.name



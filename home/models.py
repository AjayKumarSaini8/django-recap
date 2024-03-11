from django.db import models


# Create your models here.
class Mydata(models.Model):
    firstname = models.TextField(max_length=10)
    lastname = models.CharField(max_length=10)

    def __str__(self):
        return self.firstname

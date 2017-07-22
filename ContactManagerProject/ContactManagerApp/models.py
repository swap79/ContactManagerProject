from __future__ import unicode_literals
from django.db import models


class Contact(models.Model):
    FirstName = models.CharField(max_length=100,null=True)
    LastName = models.CharField(max_length=100) 
    Email = models.EmailField()
    MobileNo = models.IntegerField()

    

    def __str__(self):
        return self.FirstName

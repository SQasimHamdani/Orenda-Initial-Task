from django.db import models

# Create your models here.

import os
from django.conf import settings

def renamed_photo(self, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (self.cnic, self.name, ext)
    return os.path.join(settings.EMPLOYEE_PHOTOS_PATH, filename)


class Department(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    # image

    def __str__(self):
        return self.name


class Employee(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)

    cnic = models.CharField(max_length=13, unique=True, blank=True, null=True)

    # As mentioned in requirements to use appopriate relation.
    # Instead of ManyToOne relationship.
    # In django, ForeignKey is used.
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True,default=None)
    
    image = models.ImageField(default="", upload_to=renamed_photo, null=True, blank=True)

    def __str__(self):
        # return self.name +"_" +self.cnic
        return self.name +"_" +self.cnic
    
from django.db import models

# Create your models here.
class HRManager(models.Model):

    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True, unique=True)

    cnic = models.CharField(max_length=13, unique=True, blank=True, null=True)

    # department
    # image

    def __str__(self):
        return self.name
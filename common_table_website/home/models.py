from django.db import models

# Create your models here.
class StaffProfile(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  pronouns = models.CharField(max_length=30)
  role = models.CharField(max_length=30)
  email = models.CharField(max_length=255)
  bio = models.CharField(max_length=2000)

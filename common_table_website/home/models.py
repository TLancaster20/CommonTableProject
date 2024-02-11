from django.db import models

# Create your models here.
class StaffProfile(models.Model):
  firstname = models.CharField(max_length=255, default="")
  lastname = models.CharField(max_length=255, default="")
  pronouns = models.CharField(max_length=30, default="")
  profilepic = models.ImageField(default="static/images/profdefault.png")
  role = models.CharField(max_length=30, default="")
  email = models.EmailField(max_length=100, default="")
  bio = models.CharField(max_length=2000, default="")

class PastoralProfile(models.Model):
  firstname = models.CharField(max_length=255, default="")
  lastname = models.CharField(max_length=255, default="")
  pronouns = models.CharField(max_length=30, default="")
  profilepic = models.ImageField(default="static/images/profdefault.png")
  role = models.CharField(max_length=30, default="")
  email = models.EmailField(max_length=100, default="")
  bio = models.CharField(max_length=2000, default="")


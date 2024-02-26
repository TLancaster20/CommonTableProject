from django.db import models

# Create your models here.
class CouncilProfile(models.Model):
  firstname = models.CharField(max_length=255, default="")
  lastname = models.CharField(max_length=255, default="")
  pronouns = models.CharField(max_length=30, default="")
  profilepic = models.ImageField(default="static/images/profdefault.png")
  role = models.CharField(max_length=30, default="")
  email = models.EmailField(max_length=100, default="")
  bio = models.CharField(max_length=2000, default="")

  class Meta:
    verbose_name = "Council Profile"
    verbose_name_plural = "Council Profiles"

  def __unicode__(self):
    return '%s %s' % (self.firstname, self.lastname)


class StaffProfile(models.Model):
  firstname = models.CharField(max_length=255, default="")
  lastname = models.CharField(max_length=255, default="")
  pronouns = models.CharField(max_length=30, default="")
  profilepic = models.ImageField(default="static/images/profdefault.png")
  role = models.CharField(max_length=30, default="")
  email = models.EmailField(max_length=100, default="")
  bio = models.CharField(max_length=2000, default="")

  class Meta:
    verbose_name = "Staff Profile"
    verbose_name_plural = "Staff Profiles"

  def __unicode__(self):
    return '%s %s' % (self.firstname, self.lastname)

class PastoralProfile(models.Model):
  firstname = models.CharField(max_length=255, default="")
  lastname = models.CharField(max_length=255, default="")
  pronouns = models.CharField(max_length=30, default="")
  profilepic = models.ImageField(default="static/images/profdefault.png")
  role = models.CharField(max_length=30, default="")
  email = models.EmailField(max_length=100, default="")
  bio = models.CharField(max_length=2000, default="")

  class Meta:
    verbose_name = "Pastor Profile"
    verbose_name_plural = "Pastor Profiles"

  def __unicode__(self):
    return '%s %s' % (self.firstname, self.lastname)

class FirstTimer(models.Model):
  firstname = models.CharField(max_length=255, default="")
  lastname = models.CharField(max_length=255, default="")
  pronouns = models.CharField(max_length=30, default="")
  email = models.EmailField(max_length=100, default="")
  phonenumber = models.CharField(max_length=12, default="")
  streetaddress = models.CharField(max_length=500, default="")
  locality = models.CharField(max_length=255, default="")
  state = models.CharField(max_length=50, default="")
  zipcode = models.CharField(max_length=15, default="")
  maritalstatus = models.CharField(max_length=15, default="")

  class Meta:
    verbose_name = "First Timer"
    verbose_name_plural = "First Timers"

  def __unicode__(self):
    return '%s %s' % (self.firstname, self.lastname)


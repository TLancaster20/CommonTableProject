from django.contrib import admin
from .models import StaffProfile, PastoralProfile

#Admin == tonyb supuse42
# Register your models here.
admin.site.register(StaffProfile)
admin.site.register(PastoralProfile)
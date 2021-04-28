from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Profile)
admin.site.register(Email)
admin.site.register(Pet)
admin.site.register(AdoptedPets)
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Dog)
admin.site.register(UserDog)
admin.site.register(UserPref)

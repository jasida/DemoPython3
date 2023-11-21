from django.contrib import admin

# Register your models here.
# from . models import Place
# admin.site.register(Place)
from .models import Teams

admin.site.register(Teams)
from .models import Members

admin.site.register(Members)

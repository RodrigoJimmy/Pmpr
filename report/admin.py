from django.contrib import admin
from .models import Category, City, Location, Incident


admin.site.register([
        Category,
        City,
        Location,
        Incident
    ])

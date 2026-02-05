from django.contrib import admin
from .models import Person, Tour, Review, TouristCategory


admin.site.register(Person)
admin.site.register(Tour)
admin.site.register(Review)
admin.site.register(TouristCategory)

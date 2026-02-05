from django.urls import path
from .views import relation_db

urlpatterns = [
    path('persons/', relation_db),
]

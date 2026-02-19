from django.urls import path
from . import views

urlpatterns = [
    path('persons/', views.RelationDbView.as_view(), name='relation_db'),
]

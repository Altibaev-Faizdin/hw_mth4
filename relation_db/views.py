from django.shortcuts import render
from .models import Person
from django.views import generic




class RelationDbView(generic.ListView):
    template_name = 'relation_db.html'
    context_object_name = 'persons'
    model = Person

# def relation_db(request):
#     persons = Person.objects.all()

#     return render(
#         request,
#         'relation_db.html',
#         {
#             'persons': persons
#         }
#     )

from django.shortcuts import render
from .models import Person


def relation_db(request):
    persons = Person.objects.all()

    return render(
        request,
        'relation_db.html',
        {
            'persons': persons
        }
    )

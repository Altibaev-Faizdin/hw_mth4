from django.shortcuts import render
from django.http import HttpResponse

def quote_view(request):
    if request.method == 'GET':
        return HttpResponse(
         "Не волнуйтесь, если что-то не работает. Если бы всё работало, вас бы уволили."
"-Mosher’s Law of Software Engineering"
)
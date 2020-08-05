from django.shortcuts import render
from datetime import date
def intro(request):

    greeting = 'Hi, This is Jihye Oh and I will study Python Documentation by taking advantage Django-Project:)'
    extra_greeting = '''Hope my admission course are well solved.. plz god bless Jihye.. 🙏🏻'''
    method = '''Let views.py to templates! No single typing in templates'''
    printDate = date.today()
    context = {
        'greeting' : greeting,
        'extra_greeting' : extra_greeting,
        'method' : method,
        'printDate' : printDate,
    }
    return render(request, 'documents/00_intro.html', context)
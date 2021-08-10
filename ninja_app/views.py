from django.shortcuts import render, HttpResponse, redirect
from django.views import View
import random


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
        
    return render(request, 'home.html')

def getmoney(request, name):
    print(name)
    if name == 'FARM':
        min = 10
        max = 20
            
    elif name == 'CAVE':
        min = 5
        max = 10

    elif name == 'HOUSE':
        min = 2
        max = 5
            
    else:
        min = -50
        max = 50
        
    gold = random.randint(min, max)

    
    request.session['gold'] += gold
    request.session['activities'].append({
        'text': f'You have {"won" if gold>=0 else "lost"} {gold} golds',
        'golds': gold,
    })
    return redirect('/')
    

def reset(request):
    request.session['gold'] = 0
    return redirect('/')


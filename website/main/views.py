from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('<h2>Марусяк О.Ю</h2>')

def contact(request):
    return HttpResponse('<h2>oleh.marusiak.kn.2021@lpnu.ua</h2>')

def information(request):
    return HttpResponse('<h2>KN-208</h2>')

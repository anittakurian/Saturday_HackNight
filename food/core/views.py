from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def game(request):
    return render(request, 'game.html')

def game2(request):
    return render(request, 'game2.html')

def game3(request):
    return render(request, 'game3.html')
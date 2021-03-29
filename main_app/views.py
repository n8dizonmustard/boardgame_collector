from django.shortcuts import render
from .models import Boardgame

# Create your views here.
from django.http import HttpResponse

# Define the home view
def home(request):
    return HttpResponse('<h1>Welcome to the Board Game Collector</h1>')

def about(request):
    return render(request, 'about.html')

def boardgames_index(request):
    boardgames = Boardgame.objects.all()
    return render(request, 'bg/index.html', { 'boardgames': boardgames })

def boardgames_detail(request, boardgame_id): # boardgame_id refers to what was defined in urls.py ('boardgames/<int:boardgame_id>/')
    boardgame = Boardgame.objects.get(id=boardgame_id)
    return render(request, 'bg/detail.html', { 'boardgame': boardgame }) # :boardgame refers to the line above

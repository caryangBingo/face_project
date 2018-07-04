from django.shortcuts import render
from django.http import HttpResponse
from .models import Board

# Create your views here.


def home(request):
    # code suppressed for brevity
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    boards = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'boards': boards})

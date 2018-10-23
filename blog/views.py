from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


# Create your views here.

def home(request):
	return render(request, 'blog/home.html')

def tabuleiro(request):
	return render(request, 'blog/tabuleiro.html')

def videogame(request):
	return render(request, 'blog/videogame.html')

def obrigada(request):
	return render(request, 'blog/obrigada.html')

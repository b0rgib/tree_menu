from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu, Item

def home(request):
	return render(request, 'draw_menu/home.html', {})



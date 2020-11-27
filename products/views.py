
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from .models import person



def index(request):
	products = person.objects.all()
	return render(request, 'index.html', {'products':products})


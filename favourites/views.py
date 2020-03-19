from django.shortcuts import render,redirect
import requests

# Create your views here.
def favourites(request):
	return render(request,'favourites/favourites.html')

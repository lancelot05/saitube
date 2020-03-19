from django.shortcuts import render,redirect
import requests

# Create your views here.
def recents(request):
	return render(request,'recents/recents.html')

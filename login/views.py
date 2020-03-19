from django.shortcuts import render,redirect
import requests
from .models import User

# Create your views here.
def login(request):
	return render(request,'login/login.html')

def register(request):
	if request.method =='POST':
		name=request.POST['name']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']

		user= User.objects.create(name=name,password=password1,email=email)
		user.save();
		print('***************************************************************************')
		return redirect('/home')


	else:
		print('Get req called')
		return render(request,'login/register.html')


def toregister(request):
	return render(request,'login/register.html')
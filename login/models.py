from django.db import models
# Create your models here.
class User(models.Model):
	name=models.CharField(max_length=225)
	password=models.CharField(max_length=15)
	email	=models.EmailField(max_length=225,unique=True)
	active	=models.BooleanField(default=True)
	favourites=models.CharField(max_length=800,default="")
	recents=models.CharField(max_length=800,default="")

	USERNAME_FIELD = "email"

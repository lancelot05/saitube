from django.shortcuts import render,redirect
import requests

fav_vids_ids = []
# Create your views here.
def favourites(request, id):
	if request.method == 'POST':
		fav_vids_ids.append(id)
		print(fav_vids_ids)
	context_dict = {
		'favs' : fav_vids_ids,
	}
	return render(request,'favourites/favourites.html', context_dict)

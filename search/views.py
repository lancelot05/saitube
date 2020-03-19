from django.shortcuts import render,redirect
import requests
from isodate import parse_duration
from django.conf import settings

# Create your views here.
def index(request):
	videos=[]
	search_url='https://www.googleapis.com/youtube/v3/search'
	video_url='https://www.googleapis.com/youtube/v3/videos'
	if request.method == 'POST':
		search_params={
		'part':'snippet',
		'q': request.POST['search'],
		'key':settings.YOUTUBE_DATA_API_KEY,
		'maxResults':9,
		'type':'video'
		}
		r=requests.get(search_url,params=search_params)
		results=r.json()['items']
		video_ids=[]
		for result in results:
			video_ids.append(result['id']['videoId'])

		video_params={
		'key':settings.YOUTUBE_DATA_API_KEY,
		'part':'snippet,contentDetails,statistics',
		'id':','.join(video_ids),
		'maxResults':9,
		}

		r=requests.get(video_url,params=video_params)
		results=r.json()['items']
		for result in results:
			video_data={
				'title':title(result['snippet']['title']),
				'id':result['id'],
				'duration':duration(int(parse_duration(result['contentDetails']['duration']).total_seconds())),
				'thumbnail':result['snippet']['thumbnails']['high']['url'],
				'views':view(int(result['statistics']['viewCount'])),
				'channel_name':result['snippet']['channelTitle'],
				'pub_date':result['snippet']['publishedAt'],
				'url' : f'https://www.youtube.com/watch?v={result["id"]}'
				}
			videos.append(video_data)
			print(video_data['thumbnail'])
	context={
	'videos':videos
	}
	return render(request,'search/index.html',context)



	'''videos=[]
	if request.method=='POST':
		search_url='https://www.googleapis.com/youtube/v3/search'
		video_url='https://www.googleapis.com/youtube/v3/videos'
		search_params={
		'part':'snippet',
		'q':'learn django',
		'key':settings.YOUTUBE_DATA_API_KEY,
		'maxResults':10,
		'type':'video',
		}


		video_ids=[]
		r=requests.get(search_url,params=search_params)
		results= r.json()['items']
		for result in results:
			video_ids.append(result['id']['videoId'])

		video_params={
		'key':settings.YOUTUBE_DATA_API_KEY,
		'part':'snippet,contentDetails',
		'id':','.join(video_ids),
		'maxResults':10,
		}
		r=requests.get(video_url,params=video_params)

		results=r.json()['items']

		for result in results:
			video_data={
			'title':result['snippet']['title'],
			'id':result['id'],
			'duration':duration(int(parse_duration(result['contentDetails']['duration']).total_seconds())),
			'thumbnail':result['snippet']['thumbnails']['high']['url']
			}
			videos.append(video_data)
			print(video_data)
	context={
	'videos':videos
	}
	print(context)
	return render(request,'search/index.html',context)'''
	
def duration(s):
    h=str(int(s/3600))+":"
    s=s%3600
    m=int(s/60)
    mi=""
    s=int(s%60)
    if h=="0:":
        h=""
    if m<=9:
        mi="0"+str(m)+":"
    else:
        mi=str(m)+":"
    if s<=9:
        se="0"+str(s)
    else:
        se=str(s)
    time=h+mi+se
    return time

def title(str1):
    str2=""
    list1=[]
    if len(str1)<40:
        return str1
    else:
        for i in range(0,40):
            str2=str2+str1[i]
        str2=str2+"...."
        return str2


def view(v):
    if v>1000000000:
        v=str(round(float(v/1000000000),2))+"B"
        return v
    elif v>1000000:
        v=str(round(float(v/1000000),2))+"M"
        return v
    elif v>1000:
        v=str(round(float(v/1000),2))+"K"
        return v
    else:
        return str(v)
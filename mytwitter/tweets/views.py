from django.shortcuts import render

from django.http import HttpResponse,Http404,JsonResponse
from .models import Tweet
# Create your views here.
def home_view(request,*args,**kwargs):#for dynamic routing
    return HttpResponse("<h1>Hello Aditya</h1>")
"""
#for normal display
def tweet_detail_view(request,tweet_id,*args,**kwargs):
    try:
        obj=Tweet.objects.get(id=tweet_id)
    except:#for case when invalid(or non existing) tweet_id is entered,we raise Http404..
        raise Http404
    return HttpResponse(f"<h2>this is tweet id: {tweet_id}-{obj.content}</h2>") #TODO:check if 'f' is for foreign key or not
"""
#for displaying in Json format
def tweet_detail_view(request,tweet_id,*args,**kwargs):
    data={
        "Id":tweet_id
    }
    status=200 #if everything is fine then we will pass status as 200 to JsonResponse
    try:
        obj=Tweet.objects.get(id=tweet_id)
        data['content']=obj.content
    except:
        data['Error']="Content not found"
        status=404#if error occurs, status=404
    return JsonResponse(data,status=status)

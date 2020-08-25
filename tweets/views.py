from django.http import HttpResponse
from django.shortcuts import render

from .models import Tweet
# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse('hello world')

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    obj = Tweet.objects.get(id=tweet_id)
    return HttpResponse(f"Hello Tweet, {args} {obj.content}")

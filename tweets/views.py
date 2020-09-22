from django.http import request, Http404, JsonResponse
from django.shortcuts import render
import random

from .forms import TweetForm
from .models import Tweet
# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={})


def tweet_create_view(request, *arg, **kwargs):
    # The tweetForm class can be initialize with data or not
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        # reinitialize a blank form
        form = TweetForm()
    return render(request, 'components/form.html', context={"form": form})


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [
        {"id": x.id,
         "content": x.content,
         "likes": random.randint(0, 3433)
         } for x in qs]
    data = {
        "isUser": False,
        "listAll": tweets_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    that wil return Json
    """
    data = {
        "id": tweet_id,
        "content": obj.content,
        # "image": obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)

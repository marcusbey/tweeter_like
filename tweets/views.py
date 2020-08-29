from django.http import request, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={})

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "is_user": False,
        "response": tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIRE 
    consume by JavaScript or Swift / Java
    return Json
    """
    data = {
        "id": tweet_id,
        #"image": obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)

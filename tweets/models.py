import random
from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Tweet(models.Model):
    # keep tweets after user is deleted.
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    # many users can many tweets
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tweets")
    likes = models.ManyToManyField(
        User, related_name='tweet_user', blank=True, through=TweetLike)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.content)[0:50]

    @property
    def is_retweet(self):
        return self.parent != None

    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "content": self.content,
    #         "likes": 'random.randint(0, 200)'
    #     }

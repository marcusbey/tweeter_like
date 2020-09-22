from django import forms

from .models import Tweet


class TweetForm(forms.ModelForm):


max_tweet_length = 240
   class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self)
        content = self.cleaned_data.get("content")
        if len(content) > max_tweet_length:
            raise forms.ValidationError("This tweet is too long")
        return content 

from django.conf.urls import url

from tweets.api.views import TweetListAPIView

# from .views import (TweetDetailView, TweetListView, TweetCreateView, TweetUpdateView, TweetDeleteView)

urlpatterns = [
	url(r'^(?P<username>[\w.@+-]+)/tweet/$', TweetListAPIView.as_view(), name='list'), # /api/tweet/
]

from django.conf.urls import url

from .views import TweetListAPIView, TweetCreateAPIView, TweetLikeAPIView

# from .views import (TweetDetailView, TweetListView, TweetCreateView, TweetUpdateView, TweetDeleteView)

urlpatterns = [
	url(r'^$', TweetListAPIView.as_view(), name='list'), # /api/tweet/
	url(r'^create/$', TweetCreateAPIView.as_view(), name='create'), # /api/tweet/
	url(r'^(?P<pk>\d+)/like/$', TweetLikeAPIView.as_view(), name='like-toggle'),
]

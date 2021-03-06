from django.utils.timesince import timesince
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers

from tweets.models import Tweet
from accounts.api.serializers import UserSerializer

class ParentTweetModelSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()

	class Meta:
		model = Tweet
		fields = ['id', 'user', 'content', 'publish', 'date_display', 'timesince']

	def get_date_display(self, obj):
		return obj.publish.strftime("%b %d, at %H:%M")

	def get_timesince(self, obj):
		return timesince(obj.publish) + " ago"


class TweetSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()
	parent = ParentTweetModelSerializer(read_only=True)
	likes = serializers.SerializerMethodField()
	did_like = serializers.SerializerMethodField()

	class Meta:
		model = Tweet
		fields = ['id', 'user', 'content', 'publish', 'date_display', 
		          'timesince', 'parent', 'likes', 'did_like']

	def get_date_display(self, obj):
		return obj.publish.strftime("%b %d, at %H:%M")

	def get_timesince(self, obj):
		return timesince(obj.publish) + " ago"

	def get_likes(self, obj):
		return obj.liked.all().count()

	def get_did_like(self, obj):
		request = self.context.get("request")
		user = request.user
		if user.is_authenticated:
		  if user in obj.liked.all():
		  	return True
		return False


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

from django.utils.timesince import timesince
from rest_framework import serializers

from tweets.models import Tweet
from accounts.api.serializers import UserSerializer


class TweetSerializer(serializers.ModelSerializer):
	user = UserSerializer(read_only=True)
	date_display = serializers.SerializerMethodField()
	timesince = serializers.SerializerMethodField()
	class Meta:
		model = Tweet
		fields = ['user', 'content', 'publish', 'date_display', 'timesince']

	def get_date_display(self, obj):
		return obj.publish.strftime("%b %d, at %H:%M")

	def get_timesince(self, obj):
		return timesince(obj.publish) + " ago"

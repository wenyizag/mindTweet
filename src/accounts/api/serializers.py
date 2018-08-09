from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from tweets.models import Tweet
# from accounts.api.serializers import UserSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
	follower_count = serializers.SerializerMethodField()
	url = serializers.SerializerMethodField()
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'follower_count', 'url']

	def get_follower_count(self, object):
		return 0

	def get_url(self, object):
		return reverse_lazy('profile:detail', kwargs={'username': object.username})


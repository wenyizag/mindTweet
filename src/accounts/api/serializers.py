from rest_framework import serializers
from django.contrib.auth import get_user_model

from tweets.models import Tweet
# from accounts.api.serializers import UserSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name']

	def printuser(slef):
		return User
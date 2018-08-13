from django.test import TestCase
from django.contrib.auth import get_user_model

from accounts.models import UserProfile

User = get_user_model()

# Create your tests here.

class UserProfileTestCase(TestCase):
	def setUp(self):
		self.username = "myname"
		new_user = User.objects.create(username=self.username)

	def test_profile_created(self):
		username = self.username
		user_profile = UserProfile.objects.filter(user__username = self.username)
		self.assertTrue(user_profile.exists())
		self.assertTrue(user_profile.count() == 1)

	def test_new_user(self):
		new_user = User.objects.create(username=self.username + 'abc')


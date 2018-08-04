from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Tweet

# Create your tests here.
User = get_user_model()
class TweetTestCase(TestCase):
	def setUp(self):
		random_user = User.objects.create(username = 'Winnie')

	def test_tweet_model(self):
		obj = Tweet.objects.create(
				user = User.objects.first(),
				content = 'some random content'
			)
		self.assertTrue(obj.content == 'some random content')
		self.assertTrue(obj.id == 1)
		print(obj.pk)
		absolute_url = reverse("tweet:detail", kwargs={'pk' : obj.pk})
		self.assertEqual(absolute_url, obj.get_absolute_url())



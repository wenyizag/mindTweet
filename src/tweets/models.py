from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
import re

from .validators import validate_content

# Create your models here.

class TweetManager(models.Manager):
	def retweet(self, user, parent_obj):
		if parent_obj.parent:
			og_parent = parent_obj.parent
		else:
			og_parent = parent_obj

		obj = self.model(
				parent = og_parent,
				user = user,
				content = parent_obj.content
			)
		obj.save()

		return obj

class Tweet(models.Model):
	parent   = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL)
	user     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
	content  = models.CharField(max_length = 140, validators = [validate_content])
	updated  = models.DateTimeField(auto_now = True)
	publish  = models.DateTimeField(auto_now_add = True)

	objects = TweetManager()
	
	def __str__(self):
		return str(self.content)

	def get_absolute_url(self):
		return reverse('tweet:detail', kwargs={"pk": self.pk})

	class Meta:
		ordering = ['-publish']

def tweet_save_receiver(sender, instance, created, *args, **kwargs):
	if created and not instance.parent:
		user_regex = r'@(?P<username>[\w.@+-]+)'
		username = re.findall(user_regex, instance.content)

		hash_regex = r'#(?P<hashtag>[\w\d-]+)'
		hashtags = re.findall(hash_regex, instance.content)

post_save.connect(tweet_save_receiver, sender=Tweet)


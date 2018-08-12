from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib.auth import get_user_model
from django.views.generic import DetailView
from django.views import View
from django.db.models.signals import post_save
# Create your views here.

from .models import UserProfile

User = get_user_model()

class UserDetailView(DetailView):
	queryset = User.objects.all()
	template_name = 'accounts/user_detail.html'

	def get_object(self):
		return get_object_or_404(User, username__iexact=self.kwargs.get("username"))

	def get_context_data(self, *args, **kwargs):
		context = super(UserDetailView, self).get_context_data(*args, **kwargs)
		following = UserProfile.objects.is_following(self.request.user, self.get_object())
		context['following'] = following
		return context


class UserFollowView(View):
	def get(self, request, username, *args, **kwargs):
		toggle_user = get_object_or_404(User, username__iexact=username)
		if request.user.is_authenticated:
			is_following = UserProfile.objects.toggle_follow(request.user, toggle_user)
		return redirect("profile:detail", username=username)

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
	if created:
		new_profile = UserProfile.objects.get_or_create(user=instance)

post_save.connect(post_save_user_receiver, sender=settings.AUTH_USER_MODEL)

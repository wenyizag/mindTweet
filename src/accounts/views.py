from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.generic import DetailView
# Create your views here.

User = get_user_model()

class UserDetailView(DetailView):
	queryset = User.objects.all()
	template_name = 'accounts/user_detail.html'

	def get_object(self):
		return get_object_or_404(User, username__iexact=self.kwargs.get("username"))

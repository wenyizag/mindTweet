from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .mixins import FormUserNeededMixin, UserOwnerMixin
from .models import Tweet
from .forms import TweetModelForm
# Create your views here.

class TweetCreateView(FormUserNeededMixin, CreateView):
	template_name ='tweets/create_view.html'
	form_class = TweetModelForm
	success_url = '/tweet/create/'
	login_url = '/admin/'

class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	queryset = Tweet.objects.all()
	template_name ='tweets/update_view.html'
	form_class = TweetModelForm
	success_url = '/tweet/'

class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()

class TweetListView(ListView):
	queryset = Tweet.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		return context

class TweetDeleteView(LoginRequiredMixin, DeleteView):
	model = Tweet
	template_name ='tweets/delete_confirm.html'
	success_url = reverse_lazy('home')

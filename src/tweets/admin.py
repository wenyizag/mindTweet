from django.contrib import admin
from .forms import TweetModelForm
from .models import Tweet


class TweetAdmin(admin.ModelAdmin):
	form = TweetModelForm

admin.site.register(Tweet, TweetAdmin)

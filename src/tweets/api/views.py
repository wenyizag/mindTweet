from rest_framework import generics, permissions
from django.db.models import Q

from .serializers import TweetSerializer
from tweets.models import Tweet

# class TweetCreateAPIView(generics.ListAPIView):
# 	serializer_class = TweetSerializer

# 	def perform_create(self, serializer):
# 		serializer.save(user=self.request.user)
class TweetCreateAPIView(generics.CreateAPIView):
	serializer_class = TweetSerializer
	permission_classes = [permissions.IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class TweetListAPIView(generics.ListAPIView):
	serializer_class = TweetSerializer
	
	def get_queryset(self, *args, **kwargs):
		qs = Tweet.objects.all()
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
					Q(content__icontains=query) |
					Q(user__username__icontains=query)
					)
		return qs
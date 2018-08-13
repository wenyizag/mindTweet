from rest_framework import generics, permissions
from django.db.models import Q

from .serializers import TweetSerializer, StandardResultsSetPagination
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
	pagination_class = StandardResultsSetPagination
	
	def get_queryset(self, *args, **kwargs):
		my_follow = self.request.user.profile.get_following()
		qs1 = Tweet.objects.filter(user__in=my_follow)
		qs2 = Tweet.objects.filter(user=self.request.user)
		qs = (qs1 | qs2).distinct().order_by('-publish')
		print(self.request.GET)
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
					Q(content__icontains=query) |
					Q(user__username__icontains=query)
					)
		return qs
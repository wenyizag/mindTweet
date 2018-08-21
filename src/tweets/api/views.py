from rest_framework import generics, permissions
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response


from .serializers import TweetSerializer, StandardResultsSetPagination
from tweets.models import Tweet

# class TweetCreateAPIView(generics.ListAPIView):
# 	serializer_class = TweetSerializer

# 	def perform_create(self, serializer):
# 		serializer.save(user=self.request.user)
class TweetLikeAPIView(APIView):
	permission_classes = [permissions.IsAuthenticated]
	def get(self, request, pk, format=None):
		tweet_qs = Tweet.objects.filter(pk=pk)
		message = "Not Allowed"
		if request.user.is_authenticated:
			is_liked = Tweet.objects.like_toggle(request.user, tweet_qs.first())
			return Response({'liked': is_liked})
		return Response({'message': message}, status=400)

class TweetCreateAPIView(generics.CreateAPIView):
	serializer_class = TweetSerializer
	permission_classes = [permissions.IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class TweetListAPIView(generics.ListAPIView):
	serializer_class = TweetSerializer
	pagination_class = StandardResultsSetPagination
	
	def get_queryset(self, *args, **kwargs):
		request_user = self.kwargs.get("username")

		if request_user:
			qs = Tweet.objects.filter(user__username=request_user).order_by('-publish')
		else:
			my_follow = self.request.user.profile.get_following()
			qs1 = Tweet.objects.filter(user__in=my_follow)
			qs2 = Tweet.objects.filter(user=self.request.user)
			qs = (qs1 | qs2).distinct().order_by('-publish')

		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
					Q(content__icontains=query) |
					Q(user__username__icontains=query)
					)
		return qs
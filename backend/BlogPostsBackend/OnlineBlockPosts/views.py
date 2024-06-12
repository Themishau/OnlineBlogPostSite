from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


# Create your views here.
class LatestPostList(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()[:5]
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
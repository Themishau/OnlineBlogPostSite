from django.urls import path, include

from .views import LatestPostList

urlpatterns = [
    path('latest-posts/', LatestPostList.as_view(), name='latest_posts'),
]
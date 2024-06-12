from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "subtitle",
            "body_content",
            "get_image",
            "get_thumbnail"
        )
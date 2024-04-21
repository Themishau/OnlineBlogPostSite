from django.db import models
from django.contrib.auth.models import User
from djongo import models


# Create your models here.

class Content(models.Model):
    id = models.CharField(max_length=24, primary_key=True)
    text = models.TextField(blank=False, null=False)

    # Add other fields as needed

    def __str__(self):
        return self.id


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.EmbeddedField(
        model_container=Content
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def __str__(self):
        return self.title

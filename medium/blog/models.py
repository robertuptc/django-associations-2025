from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=255, null=True, blank=True)

class Post(models.Model):
    post = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey("User", on_delete=models.CASCADE, related_name='posts')

class Comment(models.Model):
    comment = models.CharField(max_length=255, null=True, blank=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey("User", on_delete=models.CASCADE, related_name="comments")
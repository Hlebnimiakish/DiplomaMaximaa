from django.db import models
from django.contrib.auth.models import AbstractUser



class TSUser(AbstractUser):
    email = models.EmailField(max_length=254, blank=False, unique=True)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(TSUser, on_delete=models.CASCADE, parent_link=True, null=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, parent_link=True)
    content = models.TextField()
    author = models.ForeignKey(TSUser, on_delete=models.CASCADE, parent_link=True, null=False)

    def __str__(self):
        return self.post.__str__()







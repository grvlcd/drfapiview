from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=68)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.created_at}"

from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    about = models.TextField()
    description = models.TextField()
    stack = models.TextField()
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
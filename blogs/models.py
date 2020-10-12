from django.db import models


class BlogModel(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title

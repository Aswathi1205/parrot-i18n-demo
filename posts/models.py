from django.db import models

class Post(models.Model):
    title_en = models.CharField(max_length=200)
    title_ta = models.CharField(max_length=200, blank=True)

    summary_en = models.TextField()
    summary_ta = models.TextField(blank=True)

    body_en = models.TextField()
    body_ta = models.TextField(blank=True)

    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_en
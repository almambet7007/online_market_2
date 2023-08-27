from django.db import models

# Create your models here.

class Hashtag(models.Model):
    title = models.CharField(max_length=32)


class Post(models.Model):
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    rate = models.FloatField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


#m2m
    hashtags = models.ManyToManyField(Hashtag, related_name="products")
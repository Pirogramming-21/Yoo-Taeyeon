from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    runtime = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

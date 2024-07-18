from django.db import models
from devtools.models import DevTool

class Idea(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ideas/')
    content = models.TextField()
    interest = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    devtools = models.ManyToManyField(DevTool, related_name='ideas')

    def __str__(self):
        return self.title

class IdeaStar(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('idea', 'user')
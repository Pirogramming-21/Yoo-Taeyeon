from django.db import models

class DevTool(models.Model):
    name = models.CharField(max_length=200)
    kind = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.name
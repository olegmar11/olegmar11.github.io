from django.db import models

from django.db import models
class MyModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    def str(self):
        return self.title



from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    created_by=models.ForeignKey(User, on_delete=models.CASCADE, default='')
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)

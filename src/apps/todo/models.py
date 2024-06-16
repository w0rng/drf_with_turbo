from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Task(models.Model):
    text = models.TextField()
    created_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

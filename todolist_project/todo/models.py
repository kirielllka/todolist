from django.db import models
from django.contrib.auth.models import User
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.CharField(blank=True, max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)
    complite_at = models.DateTimeField(null=True,blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

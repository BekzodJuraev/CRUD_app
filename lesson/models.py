from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class CRUD(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user} {self.text}"
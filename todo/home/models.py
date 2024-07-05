from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    username = models.CharField(max_length=120 , default="")
    password = models.CharField(max_length=120 , default="")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    id = models.AutoField(primary_key=True)

    def __str__(self) :
        return self.title
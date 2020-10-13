from django.db import models

# Create your models here.

class Taskclassification(models.Model):
    todo_text = models.CharField(max_length=200)
    todo_pred = models.CharField(max_length=50)

    def __str__(self):
        return self.todo_text

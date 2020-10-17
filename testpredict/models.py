from django.db import models
from picklefield.fields import PickledObjectField

from django.contrib.postgres.fields import JSONField


#from django.contrib.postgres.fields import JSONField
#from django.contrib.postgres.fields import JSONField
# Create your models here.

class Taskclassification(models.Model):
    todo_text = models.CharField(max_length=200)
    todo_pred = models.CharField(max_length=50)

    def __str__(self):
        return self.todo_text

class load_NLP(models.Model):
    NLP_bow=JSONField()
    def __str__(self):
        return self.NLP_bow


class load_NLP2(models.Model):
    NLP_clf=JSONField()
    def __str__(self):
        return self.NLP_clf

from django.db import models
from picklefield.fields import PickledObjectField

from django.contrib.postgres.fields import JSONField


#from django.contrib.postgres.fields import JSONField
#from django.contrib.postgres.fields import JSONField
# Create your models here.

class Taskclassification(models.Model):
    #todo_text = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    todo_pred = models.CharField(max_length=50)
    True_pred=models.CharField(max_length=50)

    #####
    completed = models.BooleanField(default=False)
    #  tag = models.CharField(max_length=50)
    #  tag_fixed = models.CharField(max_length=50)
    created_at = models.DateTimeField('投稿時間', auto_now=True)
    deadline = models.DateTimeField('〆切日時', auto_now=True)
    #####

    def __str__(self):
        return self.item

class load_NLP(models.Model):
    NLP_bow=JSONField()
    def __str__(self):
        return self.NLP_bow


class load_NLP2(models.Model):
    NLP_clf=JSONField()
    def __str__(self):
        return self.NLP_clf

#class pred_db(models.Model):
#    todo_pred=models.CharField(max_length=50)
#    True_pred=models.CharField(max_length=50)
#    def __str__(self):
#        return self.todo_pred



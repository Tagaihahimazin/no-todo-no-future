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
    #NLP_bow=models.BinaryField()
    #NLP_clf=models.BinaryField()
    NLP_bow=JSONField()
    #NLP_clf=models.JSONField()

    #NLP_bow=PickledObjectField()
    #NLP_clf=PickledObjectField()

    #NLP_bow=models.TextField(max_length=30000)

    def __str__(self):
        #return '{},{}'.format(self.NLP_bow,self.NLP_clf)
        return self.NLP_bow


class load_NLP2(models.Model):
    NLP_clf=JSONField()
    #NLP_clf=models.TextField(max_length=30000)

    def __str__(self):
        return self.NLP_clf

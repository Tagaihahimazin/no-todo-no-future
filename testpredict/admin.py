from django.contrib import admin

from .models import Taskclassification
from .models import load_NLP

# Register your models here.

admin.site.register(Taskclassification)
admin.site.register(load_NLP)

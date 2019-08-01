from django.contrib import admin

# Register your models here.
from .models import *
models=(main_category,sub_category,question_type,question)

for m in models:
   admin.site.register(m)
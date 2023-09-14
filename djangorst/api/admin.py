from django.contrib import admin

# Register your models here.

from .models import TextData        #user defined  add item from model
admin.site.register(TextData)   #user defined     for register item in adminpanel


# step 5 -OPEN ADMIN PANEL  &  ADD objects
# ------
# http://127.0.0.1:8000/admin/myapp/TextData/

# DB Browser for SQLite-Browse Data-Refresh
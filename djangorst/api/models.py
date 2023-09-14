from django.db import models

# Create your models here.
class TextData(models.Model):#user defined
    text = models.TextField()
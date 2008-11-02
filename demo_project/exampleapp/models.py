from django.db import models

class MyModel(models.Model):
    text1 = models.TextField('Text with WMD Editor', blank=False)
    text2 = models.TextField('Text without WMD Editor', blank=False)
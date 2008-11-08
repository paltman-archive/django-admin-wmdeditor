from django.contrib import admin
from .models import MyModel

from admin_wmdeditor import WmdEditorModelAdmin

class MyModelAdmin(WmdEditorModelAdmin):
    wmdeditor_fields = ('text1','text2')

admin.site.register(MyModel, MyModelAdmin)

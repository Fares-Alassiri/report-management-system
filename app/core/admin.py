from django.contrib import admin
from core.models import *

# Register your models here.

admin.site.register(Tag)
admin.site.register(Group)
admin.site.register(Profile)
admin.site.register(Report)
admin.site.register(Attachment)
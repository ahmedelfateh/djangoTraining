from django.contrib import admin
from frist_app.models import Topic, webPage, AccessRecord

# Register your models here.

admin.site.register(Topic)
admin.site.register(webPage)
admin.site.register(AccessRecord)

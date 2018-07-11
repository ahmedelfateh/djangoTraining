from django.contrib import admin
from frist_app.models import Topic, Webpage, AccessRecord, user

# Register your models here.

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(user)

from django.contrib import admin

# Register your models here.
from .models import blogEntry, comment

admin.site.register(blogEntry)
admin.site.register(comment)


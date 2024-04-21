from django.contrib import admin
from .models import Group, groupAdmin, Post

# Register your models here.
admin.site.register(groupAdmin)
admin.site.register(Group)
admin.site.register(Post)
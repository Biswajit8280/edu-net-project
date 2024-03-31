

# Register your models here.
from django.contrib import admin
from .models import Role, User, Note

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Note)

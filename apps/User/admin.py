from django.contrib import admin
from .models import Teacher,Parent,Institution,Admin
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Institution)
admin.site.register(Admin)
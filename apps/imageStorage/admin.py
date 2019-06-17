from django.contrib import admin

# Register your models here.
# posts/admin.py
from django.contrib import admin

<<<<<<< HEAD
from .models import Image

admin.site.register(Image)
=======
from .models import Image,Video

admin.site.register(Image)
admin.site.register(Video)
>>>>>>> origin/master

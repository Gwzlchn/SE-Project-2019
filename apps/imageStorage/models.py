from django.db import models

# Create your models here.


class Image(models.Model):
    name= models.CharField(max_length=500)
    imageFile= models.ImageField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.imageFile)


class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)


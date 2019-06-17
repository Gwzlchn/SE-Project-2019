from django.db import models

# Create your models here.


class Image(models.Model):
    image_id = models.IntegerField(primary_key=True,serialize=False,verbose_name="IMAGE_ID")
    name= models.CharField(max_length=500,verbose_name="IMAGE_NAME")
    imageFile= models.ImageField(upload_to='images/', verbose_name="IMAGE_URL")

    def __str__(self):
        return self.name + ": " + str(self.imageFile)


class Video(models.Model):
    video_id = models.IntegerField(primary_key=True,serialize=False,verbose_name="video_ID")
    name= models.CharField(max_length=500,verbose_name="VIDEO_NAME")
    videoFile= models.FileField(upload_to='videos/', verbose_name="VIDEO_URL")

    def __str__(self):
        return self.name + ": " + str(self.videoFile)


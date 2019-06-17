

from django.shortcuts import render
from .models import Image,Video
from .form import ImageForm,VideoForm


def showimage(request):
    lastimage = Image.objects.last()
    imagefile = lastimage.imageFile

    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'imagefile': imagefile,
               'form': form
               }

    return render(request, 'Image/imageStorageTest.html', context)





def showvideo(request):
    lastvideo = Video.objects.last()

    videofile = lastvideo.videofile

    form = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'videofile': videofile,
               'form': form
               }

    return render(request, 'Image/PostVideo.html', context)

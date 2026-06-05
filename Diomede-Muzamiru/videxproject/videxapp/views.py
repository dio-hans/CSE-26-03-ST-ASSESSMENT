from django.shortcuts import render, redirect
from .models import VideoCreation

# Create your views here.
# for uploading a video
def video_upload(request):
    if request.method == 'POST':
        form = VideoCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_grid')
    else:
        form = VideoCreation()

    context ={
        'form':form
    }  
    return render(request, 'video_upload.html', context)

# views.py


def video_landing_page(request):

    latest_videos = VideoCreation.objects.all().order_by('-date_created')

    context ={
        'videos': latest_videos

    }
    
    return render(request, 'video_grid.html', context)

def landing(request):
    if request.method == 'POST':
        return redirect('video_grid')
    else:
        return render(request, 'landing.html')

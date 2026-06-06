from django.shortcuts import render, redirect
from .models import VideoCreation
from .forms import VideoUploadForm

def video_upload(request):
    if request.method == 'POST':
    
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_grid')  
    else:
        form = VideoUploadForm()

    context = {'form': form}  
    return render(request, 'video_upload.html', context)

def video_landing_page(request):
    latest_videos = VideoCreation.objects.all().order_by('-id')
    context = {'videos': latest_videos}
    return render(request, 'video_grid.html', context)

def landing(request):
    return render(request, 'landing.html')
from django import forms
from .models import VideoCreation

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = VideoCreation
        fields = ['video_title', 'description', 'video_quality', 'date_created', 'video_file', 'thumbnail']
        
        widgets = {
            'video_title': forms.TextInput(attrs={
                'placeholder': 'Video Title',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500 text-gray-700'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description (Optional)',
                'rows': 5,
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500 text-gray-700 resize-none'
            }),
            'video_quality': forms.Select(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500 text-gray-500 bg-white appearance-none'
            }),
            'date_created': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-red-500 text-gray-500'
            }),
            
            # CRITICAL FIX: Ensure the hidden class AND the specific ID match the template label tags
            'video_file': forms.ClearableFileInput(attrs={
                'class': 'hidden', 
                'id': 'video_upload_input'
            }),
            'thumbnail': forms.ClearableFileInput(attrs={
                'class': 'hidden', 
                'id': 'thumbnail_upload_input'
            }),
        }
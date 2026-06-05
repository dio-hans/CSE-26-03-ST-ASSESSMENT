from django import forms
from .models import VideoCreation


class VideoUpload(forms.ModelForm):
    class Meta:
        model = VideoCreation
        fields = ['video_title', 'description', 'quality', 'date_created', 'thumbnail']
        widgets = {
            'product_name':forms.TextInput(attrs={'placeholder':'Video Title'}),
            'category': forms.TextInput(attrs={'placeholder':'Description (Optional)'}),
            'quantity':forms.NumberInput(attrs={'placeholder':'Video quality'}),
            'color':forms.TextInput(attrs={'placeholder':'Date of Publishing'}),
            'image_url':forms.URLInput(attrs={'placeholder':'Upload Thumbnail'}),
           
                                                  
        }
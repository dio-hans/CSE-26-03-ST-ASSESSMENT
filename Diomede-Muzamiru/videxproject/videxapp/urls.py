from django.urls import path
from . import views
urlpatterns = [
    path('video_upload/', views.video_upload, name='video_upload'),
    path('video_grid/', views.video_landing_page, name='video_grid'),
    path('', views.landing, name='landing'),

]
from django.urls import path
from .views import  SongDetailView

urlpatterns = [
        path('song/<int:id>/', SongDetailView.as_view(), name='song-detail'),
       
    ]



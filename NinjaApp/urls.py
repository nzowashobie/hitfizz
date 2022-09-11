"""NinjaApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static 
from django.conf import settings
from photo.views import PostListView, PostDetailView,homepage
from photo.views import download_view
from photo import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.startpage, name='startpage'),
    #path('RNB/',views.home, name='homepage'),
    path('RNB/',homepage.as_view(), name='downld'),
    path('RNB/download/<slug:slug>/', download_view.as_view(), name='download'),
    #path('RNB/player/<str:track_id>/' ,views.index),
    path('RNB/player/<str:_id>/',views.post_detail, name='post_detail'),
    path('Contestants/', views.bio, name='Biography'),
    path('Contestants/biography/<str:check_id>/' ,views.check), 
    path('album/item', views.album_tracks, name='album'),
    #path('album/<int:item_id>/' ,views.item, name='item'),
    #path('RNB/albums/', views.album),
    path('album/<str:_id>/',views.post_album, name='post_album'),
    path('RNB/player/<str:_id>//hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    #path('album/<int:item_id>/comments/', include('django_comments_xtd.urls')),
    path('blogpost/', PostListView.as_view(), name='posts'),
    path('blogpost/<slug:slug>/', views.detail_com, name='posts'),
    path('blogpost/<slug:slug>/', PostDetailView.as_view(), name='detail'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcounts')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    
]+ static(settings.MEDIA_URL, 
            document_root=settings.MEDIA_ROOT)

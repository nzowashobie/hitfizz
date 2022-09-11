from audioop import reverse
from email.mime import audio
from multiprocessing import context
from turtle import title
from urllib.request import Request
from django.views.generic import ListView, DetailView

#from msilib.schema import ListView
from hitcount.views import HitCountDetailView
from hitcount.views import HitCountMixin
from hitcount.models import HitCount
from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Page, PageNotAnInteger,EmptyPage, Paginator
from django.core import paginator
from django.template import loader
from .models import Post, albums,Item,Track_list
from photo.models import albums,Item
from .models import photo,Biography #import photos model
from .forms import CommentForm, blog_Form
from .forms import Comm_Form

from hitcount.views import HitCountDetailView
# Create your views here.

def startpage(request):
    return render(request, 'startpage.html')

#def homepage(request):
    #return render(request, 'homepage.html')
# rnb
#def homepage(request):
    #paginate_by=2
    #photos = photo.objects.all()
    # adding context 
   # pix= {'photos':photos}
    #return render(request, 'homepage.html', pix)
    #queryset= photo.objects.filter().order_by('-id')

def home(request):
    Photos = Track_list.objects.all().order_by('-id')
    paginator = Paginator(Photos, 5) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    
    page_obj = paginator.get_page(page_number)
    return render(request, 'homepage.html', {'page_obj': page_obj})


#biography
def bio(request):
    # imports photos and save it in database
    p = Biography.objects.all()
    # adding context 
    v= {'p':p }
    return render(request, 'contestants.html', v)

#check biography
def check(request,check_id): 
  
    # getting all the objects of hotel. 
    check_s = Biography.objects.get(name=check_id)
    #check_s = get_object_or_404(Book, id=book_id) 
    print('check_s',check_s) 
    return render(request, 'biography.html',{'bio' : check_s})

def index(request):
    return render(request, 'index.html')


def index(request,track_id):
    # imports photos and save it in database
    song = Track_list.objects.get(id=track_id)
    
    # adding context 
    print('song',song) 
    return render(request, 'index.html',{'art' : song})
    
def album_tracks(request):
   #post =  get_object_or_404(album_songs, code=code)
    template = loader.get_template('albums.html')
    context = {
        'categories' : albums.objects.all() 
    }   
    return HttpResponse(template.render(context, request))
#item
def item(request, item_id):
    template = loader.get_template('playlist.html')
    context = {
       'item' : Item.objects.get(id=item_id)           
    }   
    return HttpResponse(template.render(context, request))

#posts from users
def post_detail(request, _id):
    template_name = 'index.html'
    post = get_object_or_404(Track_list,id= _id)
    song = Track_list.objects.get(id=_id)
    comments = post.comments.filter(active=True)
    # adding context 
    count_hit = True
    
    print('song',song) 
    context = {
        'art' : Track_list.objects.get(id=_id)
    }  
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
 
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
 
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'art' : song}) 

def post_album(request, _id):
    template_name = 'playlist.html'
    posts = get_object_or_404(Item,id= _id)
    tracks = Item.objects.get(id=_id)
    comments = posts.comments.filter(active=True)
    # adding context 

    print('tracks',tracks) 
    context = {
        'item' : Item.objects.get(id=_id)
    } 
   
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = Comm_Form(data=request.POST)
        if comment_form.is_valid():
 
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = posts
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = Comm_Form()
 
    return render(request, template_name, {'posts': posts,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'item' : tracks})
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
    
class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_posts': Post.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context
        #show all comments
    

    #post comments to blog
def detail_com(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comment = Post.objects.get(slug=slug)
    comments = post.comments.filter(active=True)
    print('comz',comment) 
    context = {
        
        'list' : Post.objects.get(slug=slug)
        } 
   
   
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = blog_Form(data=request.POST)
        if comment_form.is_valid():
 
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = blog_Form()
 
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'list' : comment}) 

class homepage(ListView):
    paginate_by = 2
    model = Track_list
    context_object_name = 'downld'
    Photos = Track_list.objects.all().order_by('-id')
    template_name = 'homepage.html'

#dowload views
class download_view(HitCountDetailView):
    model = Track_list
    template_name = 'download_success.html'
    context_object_name = 'post'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(download_view, self).get_context_data(**kwargs)
        context.update({
        'popular_posts':Track_list.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context


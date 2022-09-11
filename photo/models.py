#from tkinter import Image
from dataclasses import Field, fields
from email.mime import image
from django.db import models
# Create your models here.
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount
from hitcount.models import HitCountMixin
from hitcount.settings import MODEL_HITCOUNT
from cloudinary.models import CloudinaryField
from django.utils import timezone 
from django.contrib.auth.models import User 
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from ckeditor. fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class photo(models.Model):
    id= models.IntegerField(primary_key=True,default='')
    slug = models.SlugField(max_length=200, unique=True)
    Artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    audio = CloudinaryField(resource_type ='')
    image = CloudinaryField('image')
   
    
    def __str__(self):
        return self.title

  
class Track_list(models.Model):
    #id= models.CharField(max_length=10,primary_key=True)
    ids= models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    Artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    audio = CloudinaryField(resource_type ='')
    published = models.DateField(auto_now_add=True)
    image = CloudinaryField('image')
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
    related_query_name='hit_count_generic_relation')
    
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Track_list, self).save(*args, **kwargs)

class Biography(models.Model):
    #title field
    no= models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    infor= models.TextField()
    image = CloudinaryField('image')
    def __str__(self):
         return self.name

class albums(models.Model):
    album = models.CharField(max_length=50,null=True, unique=True)
    art = CloudinaryField('Covers')
    def __str__(self):
        return  self.album

#album songs
class Item(models.Model):
    id= models.CharField(max_length=10,primary_key=True)
    album = models.CharField(max_length=50,null=True)
    Artist = models.CharField(max_length=50,null=True)
    Songs = CloudinaryField(resource_type ='')
    Title = models.CharField(max_length=50,null=True)
    category = models.ForeignKey(albums, on_delete = models.CASCADE)
    genre = models.CharField(max_length=50,null=True)
    year = models.CharField(max_length=50,null=True)
    art = CloudinaryField('albums') 
    status = models.IntegerField(choices=STATUS, default=0)
   
    def __str__(self):
        return  (self.Title)

#user track comment
class Comment(models.Model):
    post = models.ForeignKey(Track_list,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = RichTextUploadingField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
 
    class Meta:
        ordering = ['created_on']
 
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


   

#user album comment
class Comment_album(models.Model):
    post = models.ForeignKey(Item,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = RichTextUploadingField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
 
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
#blogpost
class Post(models.Model):
 
    title = models.CharField(max_length=100)
    image = CloudinaryField('image')
    description = RichTextUploadingField(blank=True, null=True)
    published = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
    related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

#comment blog
class Com_blog(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
   
    class Meta:
        ordering = ['created_on']
 
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
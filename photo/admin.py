from django.contrib import admin
# Register your models here.
from .models import Track_list, albums, photo,Biography, albums,Item
from .models import Comment
from .models import Comment_album
from .models import Post ,Com_blog
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
 
    def approve_comments(self, request, queryset):
        queryset.update(active=True)
#admin.site.register(Post)
admin.site.register(Biography)
admin.site.register(photo)
admin.site.register(albums)
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Track_list, PostAdmin)

#comment album
@admin.register(Comment_album)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']
 
    def approve_comments(self, request, queryset):
        queryset.update(active=True)
#admin.site.register(Item)
class CommentInline(admin.StackedInline):
    model = Comment_album
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Item, PostAdmin)

#comment post
@admin.register(Com_blog)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']
 
    def approve_comments(self, request, queryset):
        queryset.update(active=True)
#admin.site.register(Item)
class CommentInline(admin.StackedInline):
    model = Com_blog
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Post, PostAdmin)




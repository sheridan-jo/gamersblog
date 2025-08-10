from django.contrib import admin
from . import models
from .models import Comment

#  ModelAdmin class for the Contact model
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'last_name',
        'first_name',
        'submitted'
    )
    #  Fields are read-only in the admin panel
    readonly_fields = (
        'email',
        'last_name',
        'first_name',
        'submitted'
    )

#  Inline admin model for the Comment model
class CommentInline(admin.TabularInline):
    model = Comment  #  Shows comments related to a post in the Post's admin panel
    extra = 0  #  No extra form fields shown
    fields = ('name', 'email', 'text', 'approved')  #  Fields displayed in inline form
    readonly_fields = ('name', 'email', 'text')  #  Fields that can be seen, but not changed

#  Custom ModelAdmin for the Post model
class PostAdmin(admin.ModelAdmin):
    list_display = (  #  Fields to be displayed in the list view
        'title',
        'author',
        'status',
        'created',
        'updated',
    )

    search_fields = (  # Enables search feature
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )

    list_filter = ('status', 'topics')  #  Filters results by status and topics

    ordering = ['-created']  # Posts sorted by date created, newest first

    prepopulated_fields = {'slug': ('title',)}   # Automates generation of slugs

    #  Allows comments to be viewed directly from the Post's admin page
    #  without going to a separate screen
    inlines = [CommentInline]

#  Custom ModelAdmin for the Topic model
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']  #  Topic fields to be displayed

#  Custom ModelAdmin for the Comment model
class CommentAdmin(admin.ModelAdmin):
    list_display =  ( #  Fields displayed in list view
        'post',
        'name',
        'email',
        'approved',
        'created',
        'updated',
    )

    search_fields = (  #  Fields that can be searched
        'name',
        'email',
    )

    #  Filters list by comments that are approved and not approved
    list_filter = ('approved',)

#  Register the models
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Comment, CommentAdmin)
